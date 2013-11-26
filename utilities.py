import threading

def start(url):
	req = HeadRequest(url)
	response = urlopen(req)
	response.close()
	content=dict(response.headers.items())
	noOfThreads = 1
	size = content.get('Content-Length')
	step = int(size)//noOfThreads
	init= 0
	i=0
	l=glob.glob('*')

#list for data
	data = [None] * noOfThreads
	t = []
	if('downloads' not in l):
		system("mkdir downloads")
	fileType = content.get('Content-Type')
	fileType = fileType.split('/')
	fileNameTemp = url.split('/')
	fileNameTemp = fileNameTemp[len(fileNameTemp)-1]
	if('.' in fileNameTemp):
		fileName = "downloads/"+fileNameTemp
	else:	
		fileName = "downloads/"+fileNameTemp+'.'+fileType[1]


	f=open(fileName,"ab+")
	for i in range(noOfThreads):
		t.append(DownloadThread.D_thread(DownloadThread.download, (init, step, url, data, i)))
		t[i].start()
		init=step+init

	for i in range(noOfThreads):
		t[i].join()

	for i in range(noOfThreads):
		f.write(data[i])	

	f.close()


def pause(thread_list, download_id, data):
	f = open('.pause_data'+str(download_id), 'w')
	for i in range(len(data)-1):
		f.write(data[i])
		thread_list[i].kill()
		f.write('\n...end of a thread')
	f.write(data[len(data)-1])
	f.close()
