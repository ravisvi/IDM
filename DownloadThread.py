from threading import Thread
from urllib.request import *
from urllib.error import *

def download_file(init, step, d, i):
	try:
		req = Request(d.url, headers={'Range':'bytes=%s-%s'%(init,init+step)})
		d.data[i] = bytes(urlopen(req).read())
	
	except (HTTPError, URLError) as error:
		print('Data of %s not retrieved because %s\nURL: %s', d.fileName, error, d.url)
	except timeout:
		print('socket timed out - URL %s', d.url)
	except:
		print('What?')
	else:
		pass

def resume_download(start, end, d, i, a):
	req = Request(d.url, headers={'Range':'bytes=%s-%s'%(start,end)})
	a += bytes(urlopen(req).read())
	d.data[i] = a



class D_thread(Thread):	
	def __init__(self, download, arg) :
		Thread.__init__(self, target=download, args = arg)

	def run(self):		
		Thread.run(self)
		
	
