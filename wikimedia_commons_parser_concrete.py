import sys
import getopt
import os
import urllib.request
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import mmap
from parameters import PARAM
import pandas as pd



def main(argv):
	input_file = ""
	output_file = ""

	#process the arguments
	try:
		arguments, values = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
		if len(arguments) is not 2:
			raise ValueError()
		else:
			for argument, value in arguments:
				if argument in ("-i", "--input"):
					input_file = value
				elif argument in ("-o", "--output"):
					output_file = value		
	except (getopt.error, ValueError) as e:
		print("Wrong usage of arguments!")
		print("\tCorrect Usage: python3 scraper.py -i <input file name> -o <output file name>")
		return 0


	file_path = os.path.join(PARAM.root_filepath, "tmp_links_concrete")
	file_path = os.path.join(file_path, input_file)
	link_file = open(file_path, "r") 
	df_wikimedia = pd.DataFrame(columns=['word','caption','description','image_link','url'])

	#start parsing wikimedia for each url in file
	#count=0
	print("---> Started parsing wikimedia pages...")
	with open(file_path, "r") as file:
		for line in tqdm(file, total=get_num_lines(file_path)):
			#count+=1
			#if count == 100:
				#break
			url = line.strip().split(":::")[0]
			word = line.strip().split(":::")[1]
			cap, desc, link = parsePage(url)
			if cap==None and desc==None and link==None:
				print("wtf")
			else:
				df_wikimedia = df_wikimedia.append({'word':word,'caption':cap,'description':desc,'image_link':link,'url':url}, ignore_index=True)

	#save data to file
	print("---> Started writing data to csv file ("+ str(output_file) +")...")
	file_path = os.path.join(PARAM.root_filepath, "tmp_links_concrete_output")
	output_file_path = os.path.join(file_path, output_file)
	df_wikimedia.to_csv(output_file_path, index=False)






def parsePage(url2parse):

	#open webpage as an html tree
	try: 
		page = urllib.request.urlopen(url2parse)
		soup = BeautifulSoup(page, "html.parser")
	except:
		return None, None, None


	#find the caption
	caption = soup.find("div", attrs={"class": "wbmi-caption-value"})
	if caption is not None:
		caption = caption.text
		if caption == "Add a one-line explanation of what this file represents":
			caption = None
	#find the description
	description = soup.find("div", attrs={"class": "description mw-content-ltr en"})
	if description is not None:
		description = description.text
		if description.startswith("English:"):
			description = re.sub(r'^' + re.escape("English:"), '', description).strip(" ")
	#find the image link
	try:
		image_download_link = soup.find("div", attrs={"class": "fullImageLink"}).find("a").get("href")
	except: 
		image_download_link = None


	return caption, description, image_download_link




 
def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines





if __name__ == "__main__":
	main(sys.argv[1:])
