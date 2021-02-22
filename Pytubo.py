from pytube import Youtube

p1 = Youtube("https://www.youtube.com/watch?v=YXdOAUKCc0k")

p1.streams.first().download()