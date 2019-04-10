#!/usr/bin/python3
import sys
import csv
def tag_mapper():

    dataitems = {}
    line_number = 0

    for line in (sys.stdin):
        if line_number>0:
            parts = list(csv.reader([line]))
            vid = parts[0][0].strip()

            category = parts[0][3].strip()
            # vid_category = vedio_category+":"+vedio_id

            country = parts[0][11].strip()
            vid_country = vid+"="+country

            print("{}\t{}".format(category,vid_country))
        else:
            line_number+=1



if __name__ == "__main__":
    tag_mapper()
