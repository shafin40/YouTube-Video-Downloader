from pytube import YouTube

# Ask the user to input the video URL
video_url = input("Enter the URL of the video you want to download: ")

# Create a YouTube object with the video URL
yt = YouTube(video_url)

# Get the highest quality video stream
stream = yt.streams.get_highest_resolution()

# Download the video to the current working directory
stream.download()
