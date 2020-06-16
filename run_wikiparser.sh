#!/bin/sh

#divide the vocab into (divideby) pieces and process chunk by chunk (for memory concerns)
divideby=100
chunk=10
input_filename="tmp_urls_abstract_"
output_filename="abstract_data_"
extention=".txt"
extention_output=".csv"



python3 wikimedia_commons_parser.py -i "tmp_urls_600.txt" -o "data_600.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_601.txt" -o "data_601.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_602.txt" -o "data_602.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_603.txt" -o "data_603.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_604.txt" -o "data_604.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_605.txt" -o "data_605.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_606.txt" -o "data_606.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_607.txt" -o "data_607.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_608.txt" -o "data_608.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_609.txt" -o "data_609.csv" 

python3 wikimedia_commons_parser.py -i "tmp_urls_610.txt" -o "data_610.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_611.txt" -o "data_611.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_612.txt" -o "data_612.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_613.txt" -o "data_613.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_614.txt" -o "data_614.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_615.txt" -o "data_615.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_616.txt" -o "data_616.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_617.txt" -o "data_617.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_618.txt" -o "data_618.csv" &
python3 wikimedia_commons_parser.py -i "tmp_urls_619.txt" -o "data_619.csv"


#python3 data_divider.py $divideby

#for i in $(seq 0 $((divideby/chunk-1))
#do
#	index=$(($i*$chunk))
#	for j in $(seq 0 $((chunk-2)))
#	do
#		fileno=$(($index+$j))
#		python3 wikimedia_commons_parser_concrete.py -i "$input_filename$fileno$extention" -o "$output_filename$fileno$extention_output" &
#	done
#	fileno=$(($index+$j+1))
#	python3 wikimedia_commons_parser_concrete.py -i "$input_filename$fileno$extention" -o "$output_filename$fileno$extention_output"
#done
