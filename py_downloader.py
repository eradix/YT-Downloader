from pytube import YouTube
import sys

print()
print("======== VIDEO/MP3 DOWNLOADER =================")
print()
url =  input("Enter Youtube URL: ")
yt = YouTube(url)
print()
print("Video found: {}".format(yt.title))
print()

user_choice = int(input("Download as video or mp3? [1-video,2-mp3]: "))
filename = ""
path = ""
stream = ""

if user_choice == 1:
    print()
    print("Downloading video.....")
    print()
    filename = "{}.mp4".format(yt.title)
    path = "videos"
    stream = yt.streams.filter(res="360p").first()
elif user_choice == 2:
    print()
    print("Downloading mp3.....")
    print()
    filename = "{}.mp3".format(yt.title)
    path = "mp3"
    stream = yt.streams.filter(only_audio=True).first()
else:
    print("Invalid selection!")
    print("Please try again")
    sys.exit()
    

# Download the audio stream to the current working directory
stream.download(output_path=path, filename = filename)

print("{} downloaded successfully.".format(yt.title))
