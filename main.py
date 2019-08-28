#! /usr/bin/env python3

import tidalapi
from getpass import getpass as getpass
from sys import exit
from multiprocessing import Process, Queue
from os import system as system

def login(session: tidalapi.Session):
	
	try:
		session.login(input("Username: "), getpass())
	except:
		print("password or username is incorrect",end="")
		print(" try again")
		login(session)


def query(session: tidalapi.Session) -> tidalapi.models.SearchResult:
	
	out = input("Search for a track by name: ")
	
	if out.lower() == "quit":
		exit(0)

	search_result = session.search('track', out)
	
	return search_result

def print_result(search_result: tidalapi.models.SearchResult):
	
	i = 1
	
	for track in search_result.tracks:
		print(str(i)+" Artist: "+track.artist.name)
		print(str(i)+" Album: " +track.album.name)
		print(str(i)+" track: " +track.name)
		i+=1

def server(RTMP: Queue):
	while True:
		system("ffplay -bufsize 160000 -nodisp -loglevel quiet -autoexit \""+RTMP.get()+"\"")

def main():
	session = tidalapi.Session()
	
	login(session)
	
	track_queue = Queue()
	
	print("enter number based off of wanted track ",end="")
	print("append A if you want to append to end of ",end="")
	print("playlist, or P to play single time")
	
	if __name__ == '__main__':
		p = Process(target=server,args=(track_queue,))
		p.start()
	
	while True:
	
		search_result = query(session)
	
		print_result(search_result)
		
		selection = input("Selection requested")
		
		selection = selection.lower().strip("abcdefghijklmnopqrstuvwxyz.,;'[] ")
		num = int(selection) - 1
		track_queue.put("rtmp://"+session.get_media_url(search_result.tracks[num].id))
	
	
	

main()
