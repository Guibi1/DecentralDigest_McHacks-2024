import requests
from readability import Document
import subprocess
import os
import keyboard
import csv
import spacy

newslinkfile = "allnewslinks.csv"
goodnewslinkfile = "goodnewslinks.csv"
goodnewstitlefile = "goodnewstitles.csv"


trained_model_fr = spacy.load("title_classify_fr")
trained_model_en = spacy.load("title_classify_en")

newstitles = []
goodlinks = []


# try:
#     os.remove(newslinkfile)
#     os.remove(goodnewslinkfile)
#     os.remove(trainingset)

# finally:
#     subprocess.call(f"scrapy crawl news -o {newslinkfile}")



print("Starting Dataset Creation")
articlemax = 1200
counter = 0
with open(newslinkfile, newline='') as csvfile:

        linkreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(linkreader)

        for row in linkreader:
            
            if counter > articlemax:
                break
            try:
                response = requests.get(row[0])
                doc = Document(response.content)
                print("Title: " + doc.title())
                result_fr = (trained_model_fr(doc.title()).cats)
                result_en = (trained_model_en(doc.title()).cats)

                if (result_fr['VALID'] > result_fr['NOT_VALID'] or result_en['VALID'] > result_en['NOT_VALID']):
                    print("Valid")
                    goodlinks.append(row[0])
                    newstitles.append(doc.title())


                                    
                    
            except:
                print("Failed")
            counter+=1
    


with open(goodnewslinkfile, 'w',newline='', encoding='utf-8') as csv_file:  
    writer = csv.writer(csv_file)
    for link in goodlinks:
       writer.writerow([link])

with open(goodnewstitlefile, 'w',newline='', encoding='utf-8') as csv_file:  
    writer = csv.writer(csv_file)
    for link in newstitles:
       writer.writerow([link])



                

