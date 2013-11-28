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
	t = []
	step = d.size//d.noOfThreads        
	init= 0
	for i in range(d.noOfThreads-1):
		t.append(DownloadThread.D_thread(DownloadThread.download_file, (init, step, d, i)))
		init=step+init
		t[i].start()
	step = d.size-init
	t.append(DownloadThread.D_thread(DownloadThread.download_file, (init, step, d, d.noOfThreads-1)))
	t[d.noOfThreads-1].start()

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


def init_download(d):
	req = HeadRequest(d.url)
	response = urlopen(req)
	response.close()
	content=dict(response.headers.items())
	size = content.get('Content-Length')
	print(size)
	
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
        

def pause(thread_list, download_object):
        os.chdir('downloads')
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
        print(size)
        step = int(size)//download_object.noOfThreads
        init= 0
        i=0
        l=glob.glob('*')
        #list for data

        t = []
        f=open(download_object.fileName,"ab+")
        for i in range(download_object.noOfThreads-1):
            t.append(DownloadThread.D_thread(DownloadThread.resume_download, (init+len(a[i]), init + step, download_object, i, a[i])))
            init=step+init
            t[i].start()
            step = int(size)-init
            t.append(DownloadThread.D_thread(DownloadThread.resume_download, (init+len(a[download_object.noOfThreads-1]), init + step, download_object, download_object.noOfThreads-1, a[download_object.noOfThreads-1])))
            t[download_object.noOfThreads-1].start()
            d_size = 0
            '''for a in range(d.noOfThreads):
		t[a].join()
		d.data[a]
	'''
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

def remove(download_object):
	os.chdir('downloads')
	l = glob.glob('*')
	for a in l:
		if a == download_object.fileName:
			os.remove(a)
