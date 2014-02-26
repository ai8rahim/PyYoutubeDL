"""
# Created 26-feb-2014
# Python script to download youtube videos from local playlist
# Source: https://pypi.python.org/pypi/Pafy
"""

import sys
import pafy



if (len(sys.argv)<3):
	print "Arguments Missing:"
	print "Usage: python py-youtube-dl.py download_director playlist_file"
	sys.exit(2)

dl_dir = sys.argv[1] #'/DATA/mini/140218_'		# path to training dataset including prefix if any
pl_file = sys.argv[2] #'/DATA/mini/140218_		# path for classifier including prefix if any


playlist = open(pl_file, "r")
urls = []
for item in playlist.readlines():
	urls.append(item)
	
playlist.close()

print "Playlist " + pl_file + " imported."

for url in urls:
	video = pafy.new(url)
	best = video.getbest()
	myfilename = dl_dir + best.title + "." + best.extension
	print "Downloading... " + myfilename
	best.download(quiet = False, filepath = myfilename)
