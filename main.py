#import urllib2
from urllib.request import *

class HeadRequest(Request):
    def get_method(self):
        return "HEAD"

url = 'http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python'
req = HeadRequest(url)
response = urlopen(req)
response.close()
#print response.headers
print (response.headers.items())
content=dict(response.headers.items())
#print(type(response.headers))

#import urllib2
#url = 'http://example.com/test.zip'
noOfThreads = 4
size = content.get('Content-Length')
step = int(size)//noOfThreads
init= 0
i=0
f=open("try.html","ab+")
while(i!=noOfThreads):
	req = Request(url, headers={'Range':'bytes=%s-%s'%(init,init+step)})
	init=step+init
	i+=1	
	data = bytes(urlopen(req).read())
#	print(data,end='',file=f)
	f.write(data)
f.close()
