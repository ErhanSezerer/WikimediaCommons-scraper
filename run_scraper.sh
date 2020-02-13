#!/bin/sh


divideby=16
input_filename="tmp_vocab_"
output_filename="wikimedia_imagelinks_"
extention=".txt"

python3 data_divider.py $divideby


for i in $(seq 0 $((divideby-1)))
do
	python3 scraper.py -i "$input_filename$i$extention" -o "$output_filename$i$extention" &
done
