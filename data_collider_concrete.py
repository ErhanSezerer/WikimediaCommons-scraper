import os
import sys
from tqdm import tqdm
from parameters import PARAM
import pandas as pd




def main(dividedby):
	filename_prefix = "abstract_data_"


	#combine all files into single dict
	print("---> Started combining data from " + str(dividedby) + " parts into a single file")
	for i in tqdm(range(dividedby)):
		filename = filename_prefix + str(i) + ".csv"
		file_path = os.path.join(PARAM.root_filepath, "tmp_links_concrete_output")
		file_path = os.path.join(file_path, filename)

		if i==0:
			df_final_data = pd.read_csv(file_path)
			print(str(df_final_data.size) + "urls found in file " + str(filename))
		else:
			df_temp = pd.read_csv(file_path)
			df_final_data = df_final_data.append(df_temp, ignore_index=True) 
			print(str(df_temp.size) + "urls found in file " + str(filename))
	print("---> Started combining data from " + str(dividedby) + " parts into a single file")
	filename_prefix = "concrete_data_"
	for i in tqdm(range(dividedby)):
		filename = filename_prefix + str(i) + ".csv"
		file_path = os.path.join(PARAM.root_filepath, "tmp_links_concrete_output")
		file_path = os.path.join(file_path, filename)

		df_temp = pd.read_csv(file_path)
		df_final_data = df_final_data.append(df_temp, ignore_index=True) 
		print(str(df_temp.size) + "urls found in file " + str(filename))
	print("Total size of data: " + str(df_final_data.size))


	#save urls to file
	print("---> Started writing urls to csv file")
	path = os.path.join(PARAM.processed_datapath, "absconc_data.csv")
	df_final_data.to_csv(path, sep="\t")







if __name__ == "__main__":
	if len(sys.argv) is not 2:
		print("Wrong usage of arguments")
		print("\tCorrect usage: data_divider.py <# of chunks>")
	else:
		main(int(sys.argv[1]))
