#!/usr/bin/python3
import sys
from decimal import getcontext, Decimal
def read_map_output(file):
    for line in file:
        yield line.strip().split("\t")

def tag_reducer():
    items = {}
    for category,vid_country in read_map_output(sys.stdin):
        vid,country = vid_country.split("=")
        if category not in items.keys():
            items[category] = {vid:[country]}
        elif vid not in items[category].keys():
            items[category][vid] = [country]
        else:
            items[category][vid].append(country)

    categoryitems = {}
    for k,v in items.items():
        category_vedio_number = len(v)
        thewholeappearsnum = 0
        for sk,sv in v.items():
            thewholeappearsnum+=len(list(set(sv)))
        rate = Decimal(thewholeappearsnum/float(category_vedio_number)).quantize(Decimal('0.00'))
        print("{}\t{}".format(k,rate))



if __name__ == "__main__":
    tag_reducer()
