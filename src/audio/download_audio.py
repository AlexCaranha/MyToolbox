import pytube

video_id = "Wj7e_tzRYgk"
url = f'https://www.youtube.com/watch?v={video_id}'

# Get the YouTube video
yt = pytube.YouTube(url)

# Get the audio stream
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio file
audio_stream.download()