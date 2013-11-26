#import urllib2
from os import system
import threading
import utilities
import download


#url = 'http://r13---sn-h557sne7.googlevideo.com/videoplayback?id=cffeeb39166d8b3f&itag=18&source=picasa&ip=27.251.237.154&ipbits=0&expire=1387864459&sparams=expire,id,ip,ipbits,itag,source&signature=2B7A765A0E78E5B36692BFC6C2326CB0FEC409C9.17C4161586B13F4D2CA75ED50DB28679662F3523&key=cms1&cms_redirect=yes&ms=nxu&mt=1385272523&mv=m'

#url='http://newmedia5.directvid.com/dl/a9d97bc8930036f339171d6bc27295a1/52913752/previewnship340.mp4?'

while(1):
	url = input('Enter the url of the file you wish to download :\n')
	download_object = download.Download_object(url, 4)
	utilities.start(download_object)




#url = 'http://www.aleax.it/goo_py4prog.pdf'

