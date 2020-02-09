import sys
import os
import urllib.request
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import mmap






#global variables
root_file_path = "/media/darg1/Data/Projects/erhan_tez" #path of vocabulary and output folder
vocab_file_name = "word_vocab.txt"
limit = 1000 #number of urls to download for each keyword in dictionary
urls = {}

#supported image extensions of wikimedia commons
image_extensions = ["jpg","jpeg","jpe","png","apng","gif","tiff","tif","xcf","webp"]

#wikimedia urls
url_prefix = "https://commons.wikimedia.org"
page2parse = "https://commons.wikimedia.org/w/index.php?sort=relevance&title=Special:Search&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1"#url of advance search page








def main():
	word_counter = 0

	print("---> Started retrieving URL of images from wikimedia commons")
	file_path = os.path.join(root_file_path, vocab_file_name)
	with open(file_path, "r") as file:
		for line in tqdm(file, total=get_num_lines(file_path)):
			word_counter += 1
			word = line.strip(" ")
			searchURL = page2parse + "&limit=" + str(limit) + "&search=" + word
			count = retrieveURLs(searchURL)
			#print("Found: " + str(count) + " url(s) for " + word)
			#print(len(urls))


	#save urls to file
	print("---> Started writing urls to txt file")
	with open(os.path.join(root_file_path, "wikimediacommons_photo_links.txt"), "w") as output_file:
		for key,value in urls.items():
			output_file.write(key + "\n")
		




def retrieveURLs(url2parse):
	url_counter = 0

	try: 
		#open webpage as an html tree
		page = urllib.request.urlopen(url2parse)
		soup = BeautifulSoup(page, "html.parser")

		#find image links in the html page
		html = soup.find("ul", attrs={"class": "mw-search-results"})
		searchresults = html.find_all("table", attrs={"class": "searchResultImage"})
	except ValueError:#if the link is invalid
		return 0
	except AttributeError:
		#print("Attribute Error: search word not found")
		return 0

	for item in searchresults:
		link_suffix = item.find("a").get("href")
		if link_suffix.split(".")[-1] in image_extensions:
			urls[url_prefix+link_suffix]=0
			url_counter += 1

	return url_counter 





def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines





if __name__ == "__main__":
	main()


