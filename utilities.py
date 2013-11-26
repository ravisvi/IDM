import threading
import download
from os import system
from os import path
import threading
import glob
import DownloadThread
from urllib.request import *

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
	data = []
	for i in range(d.noOfThreads):
		data.append(None)
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
		t.append(DownloadThread.D_thread(DownloadThread.download_file, (init, step, d.url, data, i)))
		init=step+init
		t[i].start()
	step = int(size)-init
	t.append(DownloadThread.D_thread(DownloadThread.download_file, (init, step, d.url, data, d.noOfThreads-1)))
	t[d.noOfThreads-1].start()

	for i in range(d.noOfThreads):
		t[i].join()

	for i in range(d.noOfThreads):
		f.write(data[i])
	d_size = path.getsize(d.fileName)	
	if(d_size>=int(size)):
		print("Download complete")
	f.close()


def pause(thread_list, download_id, data):
	f = open('.pause_data'+str(download_id), 'w')
	for i in range(len(data)-1):
		f.write(data[i])
		thread_list[i].kill()
		f.write('\n...end of a thread')
	f.write(data[len(data)-1])
	f.close()
