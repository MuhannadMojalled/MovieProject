from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import pysrt
import assemblyai as aai

# to extract speech from movie trailers and make the subtitles


def time_to_seconds(time_obj):
    return (
        time_obj.hours * 3600
        + time_obj.minutes * 60
        + time_obj.seconds
        + time_obj.milliseconds / 1000
    )


def create_subtitle_clips(
    subtitles, videosize, fontsize=24, font="Arial", color="yellow", debug=False
):
    subtitle_clips = []

    for subtitle in subtitles:
        start_time = time_to_seconds(subtitle.start)
        end_time = time_to_seconds(subtitle.end)
        duration = end_time - start_time

        video_width, video_height = videosize

        text_clip = (
            TextClip(
                subtitle.text,
                fontsize=fontsize,
                font=font,
                color=color,
                bg_color="black",
                size=(video_width * 3 / 4, None),
                method="caption",
            )
            .set_start(start_time)
            .set_duration(duration)
        )
        subtitle_x_position = "center"
        subtitle_y_position = video_height * 4 / 5

        text_position = (subtitle_x_position, subtitle_y_position)
        subtitle_clips.append(text_clip.set_position(text_position))

    return subtitle_clips


aai.settings.api_key = "1623426ce5b74097a555588d625a1a7c"
moviepath = "Assets\Trailers\original\The Matrix (1999) Official Trailer 1 - Sci-Fi Action Movie.mp4"
transcript = aai.Transcriber().transcribe(moviepath)

subtitles = transcript.export_subtitles_srt()
movieName = "The Matrix (1999) Official Trailer 1 - Sci-Fi Action Movie.mp4"
srtname = "Assets\Trailers\srt\srt" + movieName + "_subtitle.srt"
f = open(srtname, "a")
f.write(subtitles)
f.close()

srtfilename = r"" + srtname
mp4filename = r"" + moviepath

# Load video and SRT file
video = VideoFileClip(mp4filename)
subtitles = pysrt.open(srtfilename)

begin, end = mp4filename.split(".mp4")
output_video_file = begin + "_subtitled" + ".mp4"

print("Output file name: ", output_video_file)

# Create subtitle clips
subtitle_clips = create_subtitle_clips(subtitles, video.size)

# Add subtitles to the video
final_video = CompositeVideoClip([video] + subtitle_clips)

# Write output video file
final_video.write_videofile(output_video_file)
