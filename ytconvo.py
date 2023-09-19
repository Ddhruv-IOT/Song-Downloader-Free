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
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    download_video_list = []
    with open("video_url_list.txt", "r+") as f:
        with open("downloaded.txt", "a+") as downloads:
            download_urls = [line.strip() for line in downloads.readlines()]
            video_urls = [line.strip() for line in f.readlines()]
            
            if video_urls == []:
                print("Nothing to Do... Exiting...")
                exit()
            
            for video_url in video_urls:
                if video_url in download_urls:
                    print("Nothing to do... Already resolved")
                    download_video_list.append(video_url)
                    continue
                print("Downloading...")
                download_path, name, name_no_ext = download_video(video_url, output_path="./z1")
                print("Converting...")
                ack = video_to_mp3(download_path, name, name_no_ext, "./z2")
                if ack:
                    download_video_list.append(video_url)
                    downloads.write(video_url + "\n")
                else:
                    print("Error, Skipping...")
            
            final_list = list(set(video_urls) - set(download_video_list))
            
            f.seek(0)
            
            for url in final_list:
                f.write(url + "\n")
            f.truncate()