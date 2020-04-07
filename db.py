import pymongo
import os
from Links import getLinks
from Article import  getArticle
from title import get_title
from image import Getimage
import time
from config import *

myclient = pymongo.MongoClient(CloudUri)

mydb = myclient[DatabaseName]

mycol = mydb[collectionName]


dblist = myclient.list_database_names()



collist = mydb.list_collection_names()

# It Will Insert article after 600ms

while True:
    for link in getLinks():
            TITLE = str(get_title(link).text)
            PARA = getArticle(link)
            ArticleUrl = str(link)
            IMAGEURL = str(Getimage(link))
            FinalArticle = { "title": TITLE, "para": PARA, "image": IMAGEURL ,"articleurl": ArticleUrl}
            if  mycol.find_one({"title":TITLE}):
                
                print("Article already Exist in Database Skipping it")
            else:
                try:
                    mycol.insert_one(FinalArticle)
                    print(f"Title: {TITLE} Database Inserted")
                except Exception as e :
                    print(e)
            
            
    time.sleep(600)
    





    