#!/bin/sh

#divide the vocab into (divideby) pieces and process chunk by chunk (for memory concerns)
divideby=100
chunk=10
input_filename="tmp_vocab_"
output_filename="wikimedia_imagelinks_"
extention=".txt"

python3 data_divider.py $divideby

for i in $(seq 0 $((divideby/chunk-1)))
do
	index=$(($i*$chunk))
	for j in $(seq 0 $((chunk-2)))
	do
		fileno=$(($index+$j))
		python3 scraper.py -i "$input_filename$fileno$extention" -o "$output_filename$fileno$extention" &
	done
	fileno=$(($index+$j+1))
	python3 scraper.py -i "$input_filename$fileno$extention" -o "$output_filename$fileno$extention"
done
