from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

def download_video(video_url, output_path="./z1"):

    yt = YouTube(video_url)
    # Get the highest resolution stream (you can choose different streams if you want)
    # video_stream = yt.streams.get_highest_resolution()
    video_stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    video_stream.download(output_path)
    print(f"Video downloaded to: {output_path}")
    print(output_path + "/" + video_stream.default_filename)
    return output_path, video_stream.default_filename, video_stream.default_filename.split(".")[0]

def video_to_mp3(input_video_path, video_name, v_no_ext, output_mp3_path):
    try:
        video_clip = VideoFileClip(input_video_path + "/" + video_name)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_mp3_path + "/" + v_no_ext + ".mp3", codec="mp3")
        audio_clip.close()
        # video_clip.audio.reader.close_proc()
        video_clip.close()
        print(f"Video converted to MP3: {output_mp3_path + '/' + v_no_ext + '.mp3'}")
        os.remove(input_video_path + "/" + video_name)
        print("Original video file deleted")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url_list = []
    
    with open("video_url_list.txt") as f:
        video_url_list = f.readlines()

    if video_url_list not in ["", None]:
        for video_url in video_url_list:
            download_path, name, name_no_ext = download_video(video_url, output_path="./z1")
            video_to_mp3(download_path, name, name_no_ext, "./z2")