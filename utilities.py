
import threading
#from main import set_of_downloads
import download
from os import system
from os import path
import os
import threading
import glob
import DownloadThread
from urllib.request import *
import time

class HeadRequest(Request):
    def get_method(self):
        return "HEAD"


def downNow(d):
	step = d.size//d.noOfThreads        
	init= 0
	for i in range(d.noOfThreads-1):
		d.thread_list.append(DownloadThread.D_thread(DownloadThread.download_file, (init, step, d, i)))
		init=step+init
		d.thread_list[i].start()
	step = d.size-init
	d.thread_list.append(DownloadThread.D_thread(DownloadThread.download_file, (init, step, d, d.noOfThreads-1)))
	d.thread_list[d.noOfThreads-1].start()

	os.chdir('downloads')
	f=open(d.fileName,"ab+")
	d_size = 0   
	for a in range(d.noOfThreads):
		while(d.data[a] == None):
			pass

	while(d_size<d.size):
		d_size = 0
		for a in range(d.noOfThreads):
			d_size += len(d.data[a])
			d.current_size = d_size
	

	if(d_size>=d.size):
		for i in range(d.noOfThreads):
			f.write(d.data[i])
		print("Download complete")
		#set_of_downloads.remove(d)	
	f.close()
	os.chdir('../')


def init_download(d):
	req = HeadRequest(d.url)
	response = urlopen(req)
	response.close()
	content=dict(response.headers.items())
	size = content.get('Content-Length')
	i=0
	l=glob.glob('*')
	d.size = int(size)

#list for data
	
	
	if('downloads' not in l):
		os.makedirs('downloads')
	fileType = content.get('Content-Type')
	fileType = fileType.split('/')
	fileNameTemp = d.url.split('/')
	fileNameTemp = fileNameTemp[len(fileNameTemp)-1]
	if('.' in fileNameTemp):
		fileName = fileNameTemp
	else:	
		fileName = fileNameTemp+'.'+fileType[1]
	d.fileName = fileName
        

def pause(download_object):
	if('downloads' not in os.getcwd()):
		os.chdir('downloads')
	f = open('.pause_data'+str(download_object.download_id), 'w')
	download_object.pausedFileName = f.name
	for i in range(len(download_object.data)-1):
		if(download_object.data[i] == None):
			pass
		else:
			f.write(download_object.data[i])
			download_object.thread_list[i].kill()
			f.write('xxxx...endofathreadxxxx')
	if(download_object.data[len(download_object.data)-1] == None):
		pass
	else:
		f.write(download_object.data[len(download_object.data)-1])
	download_object.paused = 1
	f.close()
	os.chdir('../')

def play(download_object):
	if('downloads' not in os.getcwd()):
		os.chdir('downloads')
	f = open(download_object.pausedFileName,'r')
	a = f.read()
	a.split('xxxx...endofathreadxxxx')
	download_object.paused = 0
	req = HeadRequest(download_object.url)
	response = urlopen(req)
	response.close()
	content=dict(response.headers.items())
	size = content.get('Content-Length')
	step = int(size)//download_object.noOfThreads
	init= 0
	i=0
	l=glob.glob('*')
	if(len(a) == 0):
		downNow(download_object)
	else:
        #list for data
		f=open(download_object.fileName,"ab+")
		for i in range(download_object.noOfThreads-1):
			download_object.thread_list.append(DownloadThread.D_thread(DownloadThread.resume_download, (init+len(a[i]), init + step, download_object, i, a[i])))
			init=step+init
			download_object.thread_list[i].start()
		step = int(size)-init
		download_object.thread_list.append(DownloadThread.D_thread(DownloadThread.resume_download, (init+len(a[download_object.noOfThreads-1]), init + step, download_object, download_object.noOfThreads-1, a[download_object.noOfThreads-1])))
		download_object.thread_list[download_object.noOfThreads-1].start()
		d_size = 0
		f=open(fileName,"ab+")
		for a in range(download_object.noOfThreads):
			while(download_object.data[a] == None):
				pass

		while(d_size<int(size)):
			d_size = 0
			for a in range(download_object.noOfThreads):
				d_size += len(download_object.data[a])
				d.current_size = d_size

		if(d_size>=int(size)):
			for i in range(download_object.noOfThreads):
				f.write(download_object.data[i])
			print("Download complete")
		#set_of_downloads.remove(d)
		f.close()
		os.chdir('../')

def remove(download_object):
	if('downloads' not in os.getcwd()):
		os.chdir('downloads')
	l = glob.glob('*')
	for a in l:
		if a == download_object.fileName:
			os.remove(a)
	os.chdir('../')
