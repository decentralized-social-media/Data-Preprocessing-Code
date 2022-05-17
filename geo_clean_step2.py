import pandas as pd
import spacy
import numpy as np
from spacy import displacy
nlp = spacy.load('en_core_web_sm')

data_df = pd.read_csv("filename")
#convert all text into string
for each in range(0,len(data_df)):
    loceach = str(data_df['location'][each])
    data_df['location'][each] = loceach
#Apply Name Entity Recognition to remove irrelevant information and eturn na value if list is empty    
data_df['location'] = data_df['location'].apply(lambda x: list(nlp(x).ents) if len(list(nlp(x).ents))> 0 else np.nan)

data_df.to_excel('filename')