import pandas as pd
import numpy as np
import re
import string

data_df = pd.read_csv("filename")

#clean html and emojis
CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

import emoji

def strip_emoji(text):
    new_text = emoji.replace_emoji(text, replace='')
    return new_text

def deEmojify(text):
    returnString = ""
    for character in text:
        try:
            character.encode("ascii")
            returnString += character
        except UnicodeEncodeError:
            returnString += ''
    return returnString

#Apply text cleaning
def clean_text_round1(text):
    text = str(text)
    text = re.sub('\[.*?\]', ' ', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

for each in range(0,len(data_df)):
    commenteach = re.sub(r"\S*https?:\S*", "", str(data_df['location'][each]))
    commenteach = cleanhtml(commenteach)
    commenteach = strip_emoji(commenteach)
    commenteach = deEmojify(commenteach)
    commenteach = clean_text_round1(commenteach)
    data_df['location'][each] = commenteach

data_df.to_excel('filename')
