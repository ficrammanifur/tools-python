from moviepy.editor import VideoFileClip

clip = VideoFileClip("video.mp4").subclip(0, 5)
clip.write_gif("output.gif")
