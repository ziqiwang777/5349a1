from pyspark import SparkContext
from ml_utils import *
import argparse


if __name__ == "__main__":
    sc = SparkContext(appName="dislikegrowth calculating")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="the input path",
                        default='file:///Users/ziqiwang/Desktop/comp5349/assignment1/Spark/')
    parser.add_argument("--output", help="the output path",
                        default='file:///Users/ziqiwang/Desktop/comp5349/assignment1/Spark/Output')
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output

    rawdata = sc.textFile(input_path + "AllVideos_short.csv")
    #vedio_id,vedio_country,trending_date,likes,dislikes,category
    moviedata = rawdata.map(extractdata1)
    # to decide which category the vedio belong to by compare the trending_date
    #vedio_id category trending_date
    category_vidiodata = rawdata.map(extractdata2)
    c_groupdata = category_vidiodata.groupByKey().filter(lambda l : l[0] != None)
    sortedby_tretime_data = c_groupdata.mapValues(lambda l : sorted(l, key = lambda x : x[1])[0])
    category_vedio = sortedby_tretime_data.map(lambda l : ((l[0],l[1][0]),1))

    #combine 2 datasets
    selected_data = category_vedio.join(moviedata).map(lambda l : ((l[0][0],l[0][1],l[1][1][3]),(l[1][1][:3])))

    sorteddata = selected_data.groupByKey().mapValues(lambda l : sorted(l,key = lambda x : x[0])[:2]).filter(lambda l : len(l[1])>1)

    dislikegrowthdata = sorteddata.map(dislikegrowth).map(lambda l : (l[1],l[0]))
    dislikegrowthdata2 = dislikegrowthdata.sortByKey(False).take(10)
    resultrdd = sc.parallelize(dislikegrowthdata2)
    result=resultrdd.map(returnresult)

    result.coalesce(1).saveAsTextFile(output_path)
