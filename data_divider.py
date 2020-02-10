import os
import sys
from parameters import PARAM






def main():
	words = []
	word_count = 0

	print("---> Started slicing data into " + str(PARAM.divideby) + " parts")

	#read the original vocabulary
	file_path = os.path.join(PARAM.root_filepath, PARAM.vocab_filename)
	vocab_file = open(file_path, "r")
	for word in vocab_file:
		words.append(word.strip(" "))
		word_count += 1
	print("word count: " + str(word_count))


	#divide it into separate files
	chunk_size = word_count // PARAM.divideby 
	for i in range(PARAM.divideby):
		chunk = []
		if i == PARAM.divideby-1:
			chunk = words[i*chunk_size:-1]
		else:
			chunk = words[i*chunk_size:i*chunk_size+chunk_size]

		file_path = os.path.join(PARAM.root_filepath, str("tmp_vocab_"+i+".txt"))
		tmp_file = open(file_path, "w")

		for word in chunk:
			tmp_file.write(word + "\n")
				







if __name__ == "__main__":
	main()
