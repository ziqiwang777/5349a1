#!/bin/bash
spark-submit \
    --master local[4] \
    dislikegrowth.py \
    --input file:///home/hadoop/ \
    --output file:///home/hadoop/rating_out/
