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
	parsePage("https://commons.wikimedia.org/wiki/File:Schwanenstein,_Lohme,_Insel_R%C3%BCgen,_170422,_ako_(3).jpg")
			








def parsePage(url2parse):
	try: 
		#open webpage as an html tree
		page = urllib.request.urlopen(url2parse)
		soup = BeautifulSoup(page, "html.parser")

		#find the data
		caption = soup.find("div", attrs={"class": "wbmi-caption-value"}).text
		description = soup.find("div", attrs={"class": "description mw-content-ltr en"}).text
		image_download_link = soup.find("div", attrs={"class": "fullImageLink"}).find("a").get("href")

	except ValueError:#if the link is invalid
		return 0
	except AttributeError:
		return 0
	except: 
		return 0


	print("---------")
	#clear the data
	if caption == "Add a one-line explanation of what this file represents":
		caption = None
	if description.startswith("English:"):
		description = re.sub(r'^' + re.escape("English:"), '', description).strip(" ")

	print(caption)
	print(description)
	print(image_download_link)


 






if __name__ == "__main__":
	main()
