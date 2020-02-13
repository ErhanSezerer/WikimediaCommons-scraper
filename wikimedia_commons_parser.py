import sys
import getopt
import os
import urllib.request
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import mmap
from parameters import PARAM



def main():
	parsePage("https://commons.wikimedia.org/wiki/File:Angel_on_bridge_of_angels_in_Rome.JPG")
	
			








def parsePage(url2parse):
	try: 
		#open webpage as an html tree
		page = urllib.request.urlopen(url2parse)
		soup = BeautifulSoup(page, "html.parser")

		#find the data
		caption = soup.find("div", attrs={"class": "wbmi-caption-value  wbmi-entityview-emptyCaption"}).text
		decription = soup.find("div", attrs={"class": "description mw-content-ltr en"}).text
		image_download_link = soup.find("div", attrs={"class": "fullImageLink"}).find("a").get("href")	

		#searchresults = html.find_all("table", attrs={"class": "searchResultImage"})
	except ValueError:#if the link is invalid
		return 0
	except AttributeError:
		#print("Attribute Error: search word not found")
		return 0
	except: 
		return 0

	print(caption)
	print(decription)
	print(image_download_link)
 












if __name__ == "__main__":
	main()
