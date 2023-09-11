video_url_list = []
    
with open("video_url_list.txt") as f:
    for line in f:
        # data = f.readline()
        print(line, end="")
    f.close()