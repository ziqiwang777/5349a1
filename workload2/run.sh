#!/bin/bash
mkdir ~/data
spark-submit \
    --master local[4] \
    dislikegrowth.py \
    --input file:///home/hadoop/data/ \
    --output file:///home/hadoop/rating_out/
