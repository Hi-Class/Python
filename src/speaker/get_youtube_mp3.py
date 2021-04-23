from pytube import YouTube
import glob
import os.path
from youtubesearchpython import VideosSearch

def youtube_audio(videoName):
	try:
		os.remove('output.mp4')
	except:
		pass

	videosSearch = VideosSearch(videoName, limit = 1)
	par = videosSearch.result()['result'][0]['link']
	yt = YouTube(par)
	yt.streams.filter(only_audio=True).first().download(filename='output')

if __name__ == '__main__':
    youtube_audio('loote lost')