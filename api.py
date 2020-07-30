#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import requests 
import pandas as pd
import json
from pandas.io.json import json_normalize

key = 'listings'
URL = 'http://marketcheck-prod.apigee.net/v2/search/car/recents?api_key=WxOyopqFPORAeROOcf3HBUH7Cc3qNuXk&dealer_id=1080226&last_seen_range=20200301-20200601&rows=50'

reponse = requests.get(URL)
json_object = reponse.json()

df = pd.DataFrame(json_normalize(json_object[key]))
print(df)

df.to_csv('newCSV.csv')

