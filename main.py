


#import urllib2
from os import system
from threading import *
import utilities
import download


#url = 'http://r13---sn-h557sne7.googlevideo.com/videoplayback?id=cffeeb39166d8b3f&itag=18&source=picasa&ip=27.251.237.154&ipbits=0&expire=1387864459&sparams=expire,id,ip,ipbits,itag,source&signature=2B7A765A0E78E5B36692BFC6C2326CB0FEC409C9.17C4161586B13F4D2CA75ED50DB28679662F3523&key=cms1&cms_redirect=yes&ms=nxu&mt=1385272523&mv=m'

#url='http://newmedia5.directvid.com/dl/a9d97bc8930036f339171d6bc27295a1/52913752/previewnship340.mp4?'

list_of_downloads = []

while(1):
	print('Enter the number of the function you want to perform : ')
	print('1. Start a new download')
	print('2. Pause')
	print('3. Play')
	print('4. Remove')
	a = int(input('Choice No : '))

	if(a == 1):
		url = input('Enter the url of the file you wish to download :\n')
		download_object = download.Download_object(url, 4)
		if(download_object in list_of_downloads):
			print("Already being downloaded")
		else:
			list_of_downloads.append(download_object)
			utilities.init_download(download_object)
			t= Thread(target=utilities.downNow, args = (download_object,))
			t.start()
	elif(a == 2):
		if(len(list_of_downloads)==1):
			if(list_of_downloads[0].paused ==0):
				utilities.pause(list_of_downloads[0])
				print('Percentage completed : ', (list_of_downloads[0].current_size//list_of_downloads[0].size)*100)
			else:
				print('Already paused')
		else:
			for i in range(len(list_of_downloads)):
				print(i+1, list_of_downloads[i].fileName)
			x = int(input('Enter the download you want to pause : '))
			if((x)>len(list_of_downloads)):
				print('Invalid choice.')
			else:
				if(list_of_downloads[x-1].paused == 0):
					utilities.pause(list_of_downloads[x-1])
					print('Percentage completed : ', (list_of_downloads[x-1].current_size//list_of_downloads[x-1].size)*100)
				else:
					print('Already paused')
	elif(a == 3):
		if(len(list_of_downloads)==1):
			if(list_of_downloads[0].paused == 1):
				utilities.play(list_of_downloads[0])
			else:
				print('Already playing')
		else:
			for i in range(len(list_of_downloads)):
				print(i+1, list_of_downloads[i].fileName)
			x = int(input('Enter the download you want to play : '))
			if((x)>len(list_of_downloads)):
				print('Invalid choice.')
			else:
				if(list_of_downloads[x-1].paused == 1):
					utilities.play(list_of_downloads[x-1])
				else:
					print('Already playing')
	elif(a == 4):
		if(len(list_of_downloads)==1):
			a = list_of_downloads[0]
			list_of_downloads.remove(a)
			utilities.remove(a)
		else:
			for i in range(len(list_of_downloads)):
				print(i+1, list_of_downloads[i].fileName)
			x = int(input('Enter the download you want to remove : '))
			if((x)>len(list_of_downloads)):
				print('Invalid choice.')
			else:
				a = list_of_downloads[x-1]
				list_of_downloads.remove(a)
				utilities.remove(a)
	else:
		print('Wrong choice')





#url = 'http://www.aleax.it/goo_py4prog.pdf'


