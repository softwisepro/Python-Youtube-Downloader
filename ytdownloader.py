# free opensource python codes examples by EricKweyunga

from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print('Title: ', yt.title)

print('views: ', yt.views)

yt = yt.streams.get_lowest_resolution()

yt.download('/workspaces/Python-Youtube-Downloader/Downloads')
