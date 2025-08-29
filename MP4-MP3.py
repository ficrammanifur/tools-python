# pip install moviepy

from moviepy.editor import VideoFileClip

video = VideoFileClip("video.mp4")
video.audio.write_audiofile("output.mp3")
