#!/bin/sh


divideby=100
input_filename="tmp_vocab_"
output_filename="wikimedia_imagelinks_"
extention=".txt"

python3 data_divider.py $divideby


for i in $(seq 1 $divideby)
do
	python3 scraper.py -i "$input_filename$i$extention" -o "$output_filename$i$extention" &
done
