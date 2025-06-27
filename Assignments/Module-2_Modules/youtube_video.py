from pytubefix import YouTube

yt = YouTube("https://www.youtube.com/watch?v=6d5SS0gS5bU", use_po_token=True)
stream = yt.streams.get_highest_resolution()
stream.download()
