#!/usr/bin/env python3
print("Content-Type: text/html")
print()
import pafy
import bs4
import requests
import sys
import ssl
import cgi

#sys.stderr = sys.stdout

#print "enter any song u want to download : song and then artist"
#song = raw_input()
#artist = raw_input()

def main():
	form = cgi.FieldStorage()
	song = form.getvalue("song", "error")
	#song = input()
	artist = form.getvalue("artist", "error")
#	artist = input()

	str11 = 'https://www.youtube.com/results?search_query='
	str1 = str11 + '+' + song + "+"+ artist + '+'
	res = requests.get(str1)
	list1 = []
	html = res.content
	soup = bs4.BeautifulSoup(html)
	elems = soup.select('button li')
	for i in elems:
		i = str(i)
		str2 =  i[153:164]
		if str2.startswith('=') is False:  
			list1.append(str2)

	url = "https://www.youtube.com/watch?v="
	#print list1
	video = pafy.new(url + list1[2])
	#print video.title
	#print video.length
	#print video.rating
	audiostreams = video.m4astreams
	if audiostreams is []:
		audiostreams = video.oggstreams
	 #       for a in audiostreams:
		         #print(a.extension, a.bitrate, a.get_filesize())
		         #print a.extension
	audiostreams[0].download()
	x = "http://localhost/" +audiostreams[0].title + ".m4a"
	print(x)
		
main()

