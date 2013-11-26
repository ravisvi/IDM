import threading
class download_object:
	download_id = 0 
	def __init__(self, url):
		if(download_id<2999):
			self.download_id += 1
		else
			self.download_id = 0
		self.url = url
		