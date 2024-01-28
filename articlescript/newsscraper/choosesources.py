import requests
from readability import Document
import subprocess
import os
import keyboard
import csv
import spacy
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import json
import time
from io import StringIO
from html.parser import HTMLParser
from datetime import date

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

goodnewslinkfile = "goodnewslinks.csv"
goodnewstitlefile = "goodnewstitles.csv"
emptywordsfile = "emptywords.csv"

links = []
titles = []
emptywords = []
wordcount = {}
tags = []

# Load empty words
with open(emptywordsfile, 'r') as file:
    for line in file:
        emptywords.append(line.strip().lower())

# Load links
with open(goodnewslinkfile, 'r') as file:
    for line in file:
        links.append(line.strip())

# Process titles and count words
with open(goodnewstitlefile, 'r') as file:
    for line in file:
        querywords = line.replace('"', '').replace(',', '').replace(':', '').replace('|', '').split()
        resultwords = [word for word in querywords if word.lower() not in emptywords]

        for word in resultwords:
            word_lower = word.lower()
            wordcount[word_lower] = wordcount.get(word_lower, 0) + 1

        result = ' '.join(resultwords)
        titles.append(result)

# Determine top 50 words
sorted_by_word_count = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)
tags_words = set(dict(sorted_by_word_count[:75]).keys())

# Filter words based on top 50 words
tags = []
for title in titles:
    querywords = title.split()
    taggedwords = [word for word in querywords if word.lower() in tags_words]
    tags.append(taggedwords)


def choose_articles():
    links_with_keywords = {}

    # Store words for each link
    for tag_list, link in zip(tags, links):
        links_with_keywords[link] = set(tag_list)

    # Find groups of links with at least 2 common keywords
    common_links_groups = []
    for link1, keywords1 in links_with_keywords.items():

        for link2, keywords2 in links_with_keywords.items():
            if link1 != link2:
                common_keywords = keywords1.intersection(keywords2)
                if len(common_keywords) >= 2:
                    # Create a group for these links
                    group = {link1, link2}
                    all_keywords_in_group = set(common_keywords)  # start with common keywords
                    # Check for other links sharing these common keywords
                    for other_link, other_keywords in links_with_keywords.items():
                        if other_link not in group and common_keywords.issubset(other_keywords):
                            group.add(other_link)
                            all_keywords_in_group.update(other_keywords)  # add all keywords of the link
                    # Check if this group has 3+ unique keywords
                    if len(all_keywords_in_group) >= 3:
                        # Check if this group is a superset of an existing group or is not a subset of any existing group
                        if not any(group.issubset(existing_group) or existing_group.issubset(group) for existing_group, _ in common_links_groups):
                            common_links_groups.append((group, all_keywords_in_group))

    return common_links_groups

# Get groups of links with common keywords and print them
links_with_common_keywords = choose_articles()
# for group, all_keywords in links_with_common_keywords:
#     print(f"All Keywords: {all_keywords}, Links: {group}")

all_groups = []
keywords_group = []
for group, keywords in links_with_common_keywords:
    all_groups.append(group)
    keywords_group.append(keywords)


def mistralInput(linkgroup,keywordsforarticle):
    output = "Keywords: " + str(keywordsforarticle) + "\n"
    for link in linkgroup:
        response = requests.get(link)
        doc = Document(response.content)
        output+=("\nLink: " + link + "\n Article: " + (strip_tags(doc.summary())))

    return output



model = "mistral-medium"

client = MistralClient(api_key="0w3q8F4BCcpsHmEpjsBzrZ8NfjVTVeSD")

def writearticle(functioninput,sources):

    # Use the original text for unbiased and modified for the biased versions
    unbiased_messages = [ChatMessage(role="user", content="Write an unbiased article taking in the common information from each article and making sure the article is in line with keywords said in the beginning" + functioninput + "Write an unbiased article taking in the common information from each article and making sure the article is in line with keywords said in the beginning")]
    chat_response_unbiased = client.chat(model=model, messages=unbiased_messages)
    keyword_content = chat_response_unbiased.choices[0].message.content
    title_message = [ChatMessage(role="user", content="Write a non click bate accurate title for without anything else but the title: " +  keyword_content + "JUST THE TITLE NOTHING ELSE")]
    title = client.chat(model=model, messages=title_message)
    title_content = title.choices[0].message.content



    json_data = {
        "title": title_content,
        "date": date.today(),
        "text": keyword_content,
        "sources": sources
    }

    # Print the JSON string
    
    return json_data

mistralin,keywordin = all_groups[0],keywords_group[0]
mistraltext = mistralInput(mistralin,keywordin)
finalarticle = writearticle(mistraltext,keywordin)
print(finalarticle)


