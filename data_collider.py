import os
import sys
from tqdm import tqdm
from parameters import PARAM




def main(dividedby):
	urls = {}
	filename_prefix = "wikimedia_imagelinks_"


	#combine all files into single dict
	print("---> Started combining data from " + str(dividedby) + " parts into a single file")
	for i in tqdm(range(dividedby)):
		count=0
		filename = filename_prefix + str(i) + ".txt"
		file_path = os.path.join(PARAM.root_filepath, filename)
		vocab_file = open(file_path, "r")
		for url in vocab_file:
			count+=1
			urls[url] = 0
		#print(str(count) + "urls found in file " + str(filename))
	print("Total size of urls: " + str(len(urls)))


	#save urls to file
	print("---> Started writing urls to txt file")
	with open(os.path.join(PARAM.root_filepath, PARAM.output_filename), "w") as output_file:
		for key,value in urls.items():
			output_file.write(key)







if __name__ == "__main__":
	if len(sys.argv) is not 2:
		print("Wrong usage of arguments")
		print("\tCorrect usage: data_divider.py <# of chunks>")
	else:
		main(int(sys.argv[1]))
