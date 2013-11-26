from threading import Thread
from urllib.request import *

def download_file(init, step, url, data, i):
	try:
		req = Request(url, headers={'Range':'bytes=%s-%s'%(init,init+step)})
		data[i] = bytes(urlopen(req).read())
	except (HTTPError, URLError) as error:
		print('Data of %s not retrieved because %s\nURL: %s', name, error, url)
	except timeout:
		print('socket timed out - URL %s', url)
	except:
		print('What?')
	else:
		pass

class D_thread(Thread):	
	def __init__(self, download, arg) :
		Thread.__init__(self, target=download, args = arg)

	def run(self):		
		Thread.run(self)
		
	
