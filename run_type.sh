#!/usr/bin/bash

# ./run_type.sh docs/hyf/ru_guo_mei_you_ni.txt result/hyf/ru_guo_mei_you_ni/

sample_file_path=$1

result_file_path_prefix=$2

python3 lac_train.py $sample_file_path a $result_file_path_prefix/a 
python3 lac_train.py $sample_file_path b $result_file_path_prefix/b 
python3 lac_train.py $sample_file_path c $result_file_path_prefix/c 
python3 lac_train.py $sample_file_path d $result_file_path_prefix/d 