import requests
from readability import Document
import subprocess
import os
import keyboard
import csv

newslinkfile = "allnewslinks.csv"
goodnewslinkfile = "goodnewslinks.csv"
trainingsetvalid = "trainingsetvalid.csv"
trainingsetnotvalid = "trainingsetnotvalid.csv"

newstitles = []
othertitles = []
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
                while True:  # making a loop
                    if keyboard.is_pressed('left'):  # if key 'q' is pressed 
                        print('Valid News')
                        newstitles.append(doc.title())
                        goodlinks.append(row[0])
                        break  # finishing the loop
                    elif keyboard.is_pressed('right'):
                        print('Not Valid News')
                        othertitles.append(doc.title())
                        break  # finishing the loop
                    
                    
            except:
                print("Failed")
            counter+=1
    
            


with open(trainingsetvalid, 'w',newline='', encoding='utf-8') as csv_file:  
    writer = csv.writer(csv_file)
    for title in newstitles:
       writer.writerow([title])
       counter+=1

with open(trainingsetnotvalid, 'w',newline='', encoding='utf-8') as csv_file:  
    writer = csv.writer(csv_file)
    for title in othertitles:
       writer.writerow([title])
       counter+=1

with open(goodnewslinkfile, 'w',newline='', encoding='utf-8') as csv_file:  
    writer = csv.writer(csv_file)
    for link in goodlinks:
       writer.writerow([link])


                

