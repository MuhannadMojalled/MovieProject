from moviepy.editor import *

# Load the mp4 file
video = VideoFileClip(
    "Back To The Future (1985) Theatrical Trailer - Michael J Fox Movie HD.mp4"
)

# Extract audio from video
video.audio.write_audiofile(
    "Back To The Future (1985) Theatrical Trailer - Michael J Fox Movie HD.mp3"
)
