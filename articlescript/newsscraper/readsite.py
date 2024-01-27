import requests
from readability import Document
import subprocess
import os
newslinkfile = "newslinks.csv"
try:
    os.remove(newslinkfile)
finally:
    subprocess.call(f"scrapy crawl news -o {newslinkfile}")



# response = requests.get('https://www.lapresse.ca/actualites/chroniques/2024-01-27/eviter-la-distraction-ou-la-deception.php')
# doc = Document(response.content)
# print(doc.title())
# print(doc.summary())

# with open("tEST.html", "w") as text_file:
#     text_file.write(doc.summary())