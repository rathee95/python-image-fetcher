import os
import requests
from urllib.parse import urljoin 
from bs4 import BeautifulSoup
import sys

def downloader(url):
	domain = url.split('//')[-1].split('/')[0]
	os.makedirs(domain)
	response = requests.get(url)
	if(response.status_code != 200):
		return
	soup = BeautifulSoup(response.text)
	img_tags = soup.find_all('img')
	image_source_paths = set() 
	for i in img_tags:
		src = i.get('src')
		if not src:
			continue
		if src[:7] == 'http://' or src[:8] == 'https://':
			image_source_paths.add(src)
		else:
			image_source_paths.add(urljoin(url,src))
	i = 0		
	for img_url in image_source_paths:
		try:
			re = requests.get(img_url)
		except:
 			continue
 		
		i = i + 1
		filename = str(i) + "." + img_url.split('.')[-1]
		f = open(domain+'/'+filename,'wb')
		f.write(re.content)
		f.close()

if __name__ == '__main__':		
	if len(sys.argv) < 2:
		print("enter a url from which to get images, say http://www.blah.com or https://ww.blah.com along with the file name, ie python3 download_images.py http://blah.com ")
	else:
		downloader(sys.argv[1])



	
