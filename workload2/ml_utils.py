import csv

def dislikegrowth(record):
    line1 = record[1][0]
    line2 = record[1][1]
    dislikegrowth = (int(line2[2]) - int(line1[2])) - (int(line2[1])-int(line1[1]))
    return(record[0],int(dislikegrowth))

def extractdata1(record):
    try:
        recordlist = record.split(",")
        vedio_id = str(recordlist[0]).strip()
        trending_datelist= str(recordlist[1].strip()).split(".")
        trending_date = trending_datelist[0]+trending_datelist[2]+trending_datelist[1]
        likes = str(recordlist[6]).strip()
        dislikes = str(recordlist[7]).strip()
        vedio_country = str(recordlist[11]).strip()
        vedio_category = str(recordlist[3]).strip()
        return((vedio_id,vedio_category),(trending_date,likes,dislikes,vedio_country))
    except:
        return(None,None)
def extractdata2(record): # extract vedio_id category trending_date
    try:
        recordlist = record.split(",")
        vedio_id = str(recordlist[0]).strip()
        trending_datelist= str(recordlist[1].strip()).split(".")
        trending_date = trending_datelist[0]+trending_datelist[2]+trending_datelist[1]
        # views = str(recordlist[5]).strip()
        vedio_category = str(recordlist[3]).strip()
        return(vedio_id,(vedio_category,trending_date))
    except:
        return(None,None)

def returnresult(record):
    result = ""
    result = record[1][0]+","+str(record[0])+","+record[1][1]+","+record[1][2]
    return result
