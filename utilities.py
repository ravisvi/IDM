import threading
#from main import set_of_downloads
import download
from os import system
from os import path
import threading
import glob
import DownloadThread
from urllib.request import *
import time

class HeadRequest(Request):
    def get_method(self):
        return "HEAD"


def start(d):
	req = HeadRequest(d.url)
	response = urlopen(req)
	response.close()
	content=dict(response.headers.items())
	noOfThreads = 1
	size = content.get('Content-Length')
	print(size)
	step = int(size)//d.noOfThreads
	init= 0
	i=0
	l=glob.glob('*')

#list for data
	
	t = []
	if('downloads' not in l):
		system("mkdir downloads")
	fileType = content.get('Content-Type')
	fileType = fileType.split('/')
	fileNameTemp = d.url.split('/')
	fileNameTemp = fileNameTemp[len(fileNameTemp)-1]
	if('.' in fileNameTemp):
		fileName = "downloads/"+fileNameTemp
	else:	
		fileName = "downloads/"+fileNameTemp+'.'+fileType[1]
	d.fileName = fileName

	
	for i in range(d.noOfThreads-1):
		t.append(DownloadThread.D_thread(DownloadThread.download_file, (init, step, d, i)))
		init=step+init
		t[i].start()
	step = int(size)-init
	t.append(DownloadThread.D_thread(DownloadThread.download_file, (init, step, d, d.noOfThreads-1)))
	t[d.noOfThreads-1].start()

	d_size = 0

	'''for a in range(d.noOfThreads):
		t[a].join()
		d.data[a]
		'''
	f=open(fileName,"ab+")
	for a in range(d.noOfThreads):
		d_size += len(d.data[a])
	while(d_size<int(size)):
		for a in range(d.noOfThreads):
			d_size += len(d.data[a])
	

	if(d_size>=int(size)):
		for i in range(d.noOfThreads):
			f.write(d.data[i])
		print("Download complete")
		#set_of_downloads.remove(d)	
	f.close()


def pause(thread_list, download_object):
	f = open('.pause_data'+str(download_object.download_id), 'w')
	download_object.pausedFileName = f.name()
	for i in range(len(download_object.data)-1):
		f.write(download_object.data[i])
		thread_list[i].kill()
		f.write('xxxx...endofathreadxxxx')
	f.write(download_object.data[len(download_object.data)-1])
	download_object.paused = 1
	f.close()

def play(download_object):
	f = open(download_object.pausedFileName,'r')
	a = f.read()
	a.split('xxxx...endofathreadxxxx')
	d.paused = 0

	req = HeadRequest(d.url)
	response = urlopen(req)
	response.close()
	content=dict(response.headers.items())
	size = content.get('Content-Length')
	print(size)
	step = int(size)//d.noOfThreads
	init= 0
	i=0
	l=glob.glob('*')

#list for data
	
	t = []
	if('downloads' not in l):
		system("mkdir downloads")
	fileType = content.get('Content-Type')
	fileType = fileType.split('/')
	fileNameTemp = d.url.split('/')
	fileNameTemp = fileNameTemp[len(fileNameTemp)-1]
	if('.' in fileNameTemp):
		fileName = "downloads/"+fileNameTemp
	else:	
		fileName = "downloads/"+fileNameTemp+'.'+fileType[1]
	d.fileName = fileName

	f=open(fileName,"ab+")
	for i in range(d.noOfThreads-1):
		t.append(DownloadThread.D_thread(DownloadThread.resume_download, (init+len(a[i]), init + step, d, i, a[i])))
		init=step+init
		t[i].start()
	step = int(size)-init
	t.append(DownloadThread.D_thread(DownloadThread.resume_download, (init+len(a[d.noOfThreads-1]), init + step, d, d.noOfThreads-1, a[d.noOfThreads-1])))
	t[d.noOfThreads-1].start()

	d_size = path.getsize(d.fileName)	
	while(d_size<int(size)):
		d_size = path.getsize(d.fileName)	
	if(d_size>=int(size)):
		for i in range(d.noOfThreads):
			f.write(d.data[i])
		print("Download complete")
		#set_of_downloads.remove(d)	
	f.close()





