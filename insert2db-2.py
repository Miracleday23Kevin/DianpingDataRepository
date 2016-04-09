from pymongo import MongoClient
import os
import json
# variables with 's' as initial indicates that it regards the 'Shops' section.
# prepare list of filenames
dirpath = "/home/ubuntu/user/Data"
sdirpath=dirpath+'/Shops'
filelist = os.listdir(dirpath)
sfilelist=os.listdir(sdirpath)
# prepare database
client = MongoClient("mongodb://tonyxuan2.cloudapp.net:27017")
db = client['dianping']
# handle files one by one
count = 0
scount=0
error_count = 0
serror_count=0
for one in filelist:
    #count += 1
    #print(count)
    if not one.endswith("txt"):
        continue
    count += 1
    if one.endswith("_profile.txt"):
        try:
            f = open(dirpath + "/" + one)
            j = json.load(f)
            f.close()
            db.user_profiles.insert_one(j)
            continue
        except:
            error_count += 1
            print("An error occured when adding a user's profile.")
    if one.endswith("_reviews.txt"):
        try:
            f = open(dirpath + "/" + one)
            j = json.load(f)
            f.close()
            ID = one.split("_")[0]
            j["ID"] = ID
            db.user_reviews.insert_one(j)
            continue
        except:
            error_count += 1
            print("An error occured when adding a user's reviews.")
    if one.endswith("_checkins.txt"):
        try:
            f = open(dirpath + "/" + one)
            j = json.load(f)
            f.close()
            ID = one.split("_")[0]
            j["ID"] = ID
            db.user_checkins.insert_one(j)
            continue
        except:
            error_count += 1
            print("An error occured when adding a user's checkins.")
    if one.endswith("_fans.txt"):
        try:
            f = open(dirpath + "/" + one)
            j = json.load(f)
            f.close()
            ID = one.split("_")[0]
            j["ID"] = ID
            db.user_fans.insert_one(j)
            continue
        except:
            error_count += 1
            print("An error occured when adding a user's fans.")
    if one.endswith("_follows.txt"):
        try:
            f = open(dirpath + "/" + one)
            j = json.load(f)
            f.close()
            ID = one.split("_")[0]
            j["ID"] = ID
            db.user_follows.insert_one(j)
            continue
        except:
            error_count += 1
            print("An error occured when adding a user's follows.")
for one in sfilelist:
    scount+=1
    #print('s'+str(scount))
    try:
        f = open(sdirpath + "/" + one)
        j = json.load(f)
        f.close()
        db.shops.insert_one(j)
        continue
    except:
        serror_count += 1
        print("An error occured when adding a Shop profile.")
        
print("done")
print("user section:")
print("total: " + str(count))
print("error: " + str(error_count))
print("Shops section:")
print("stotal: " + str(scount))
print("serror: " + str(serror_count))
