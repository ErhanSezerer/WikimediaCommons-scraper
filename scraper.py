import sys
import getopt
import os
import urllib.request
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import mmap
from parameters import PARAM








def main(argv):

	#process the arguments
	try:
		arguments, values = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
		if len(arguments) is not 2:
			raise ValueError()
		else:
			for argument, value in arguments:
				if argument in ("-i", "--input"):
					PARAM.vocab_filename = value
				elif argument in ("-o", "--output"):
					PARAM.output_filename = value		
	except (getopt.error, ValueError) as e:
		print("Wrong usage of arguments!")
		print("\tCorrect Usage: python3 scraper.py -i <input file name> -o <output file name>")
		return 0



	#parse vocab file and retrieve each image associated with it
	word_counter = 0
	print("---> Started retrieving URL of images from wikimedia commons")
	file_path = os.path.join(PARAM.root_filepath, PARAM.vocab_filename)
	with open(file_path, "r") as file:
		for line in tqdm(file, total=get_num_lines(file_path)):
			word_counter += 1
			word = line.strip(" ")
			searchURL = PARAM.page2parse + "&limit=" + str(PARAM.limit) + "&search=" + word
			count = retrieveURLs(searchURL)
			#print("Found: " + str(count) + " url(s) for " + word)
			#print(len(urls))


	#save urls to file
	print("---> Started writing urls to txt file")
	with open(os.path.join(PARAM.root_filepath, PARAM.output_filename), "w") as output_file:
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
		if link_suffix.split(".")[-1] in PARAM.image_extensions:
			urls[PARAM.url_prefix+link_suffix]=0
			url_counter += 1

	return url_counter 





def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines




urls = {}
if __name__ == "__main__":
	main(sys.argv[1:])


