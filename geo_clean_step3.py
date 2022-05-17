import pandas as pd
import numpy as np
from spacy import displacy
from collections import Counter
from geopy.geocoders import Nominatim

data_df = pd.read_csv("filename")
#Request for Nominatim service
geolocator = Nominatim(user_agent='specify agent name here')
#Convery geolocation information into the standard format
for each in range(0,len(data_df)):
    if (str(data_df["location"][each]) != "nan"):
        data_df["location"][each] = geolocator.geocode(data_df["location"][each],language="en")
data_df.to_excel('filename')