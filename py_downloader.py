from pytube import YouTube
import sys
import os

print()
print("======== VIDEO/MP3 DOWNLOADER =================")
print()
url =  input("Enter Youtube URL: ")
yt = YouTube(url)
print()
print("Video found: {}".format(yt.title))
print()

user_choice = int(input("Download as video or mp3? [1-video,2-mp3]: "))
stream = ""
print()

# Get the download path from the user
download_path = input("Enter the download path(absolute path): ")

# Make sure the directory exists
if not os.path.exists(download_path):
    os.makedirs(download_path)

if user_choice == 1:
    print()
    print("Downloading video.....")
    print()
    stream = yt.streams.get_highest_resolution()
    stream.download(download_path)
elif user_choice == 2:
    print()
    print("Downloading mp3.....")
    print()
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(download_path)
    os.rename(f"{download_path}\\{yt.title}.mp4", f"{download_path}\\{yt.title}.mp3")
else:
    print("Invalid selection!")
    print("Please try again")
    sys.exit()
    

# Download the audio stream to the current working directory
print("{} downloaded successfully.".format(yt.title))
