"""
# Created 26-feb-2014
# Python script to download youtube videos from local playlist
# Source: https://pypi.python.org/pypi/Pafy
# Author: ai8rahim
"""

import sys
import pafy


# check for arguments
if (len(sys.argv)<3):
	print "Arguments Missing:"
	print "Usage: python py-youtube-dl.py download_directory playlist_file"
	sys.exit(2)

dl_dir = sys.argv[1] 	# download directory
pl_file = sys.argv[2]	# playlist file location


playlist = open(pl_file, "r")
urls = []
for item in playlist.readlines():	# retrieve urls from the playlist
	urls.append(item)
	
playlist.close()

print "Playlist " + pl_file + " imported."

for url in urls:	# download all videos in the best format available
	video = pafy.new(url)
	best = video.getbest()
	myfilename = dl_dir + best.title + "." + best.extension
	print "Downloading... " + myfilename
	best.download(quiet = False, filepath = myfilename)
