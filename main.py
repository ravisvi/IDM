#import urllib2
from urllib.request import *

class HeadRequest(Request):
    def get_method(self):
        return "HEAD"

url = 'http://r13---sn-h557sne7.googlevideo.com/videoplayback?id=cffeeb39166d8b3f&itag=18&source=picasa&ip=27.251.237.154&ipbits=0&expire=1387864459&sparams=expire,id,ip,ipbits,itag,source&signature=2B7A765A0E78E5B36692BFC6C2326CB0FEC409C9.17C4161586B13F4D2CA75ED50DB28679662F3523&key=cms1&cms_redirect=yes&ms=nxu&mt=1385272523&mv=m'
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
fileType = content.get('Content-Type')
fileType = fileType.split('/')
fileName = "try"+'.'+fileType[1]
f=open(fileName,"ab+")
while(i!=noOfThreads):
	req = Request(url, headers={'Range':'bytes=%s-%s'%(init,init+step)})
	init=step+init
	i+=1	
	data = bytes(urlopen(req).read())
#	print(data,end='',file=f)
	f.write(data)
f.close()
