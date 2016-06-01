# -*- coding: utf-8 -*-
"""
Created on Fri May 27 13:20:34 2016

@author: april.liu
"""

import pandas as pd
from sqlalchemy import create_engine


# Create Connection Engines to Stingray and Redshift 
engine_RS = create_engine('postgresql://username:pwd@10.0.7.23:5439/rmus_prod') 
Listing_Info_Query = ''' select 
UPPER(city), 
state_code, 
zip, 
business_market_id, 
property_type,
count(listing_id)
from edw.listing_dim
where search_status IN ('Sold','Active') and business_market_id IN (select
business_market_id
from edw.business_market_dim
where business_market_name = 'Little Rock') and list_price_amount > 250000
and (listing_date >= '2015-03-01' or listing_added_date >= '2015-03-01')
group by UPPER(city), state_code, zip, property_type, business_market_id
order by count(listing_id) asc '''

listing_info = pd.read_sql(Listing_Info_Query, con = engine_RS)

upper = listing_info['upper']
listing_info_list = []
listing_info_lst = []
for j in upper:
    if j is not None:
        if j not in listing_info_lst:
            listing_info_lst.append(j)
            listing_info_list.append(j.split())

zip_name = listing_info['zip']     
zip_list = []
zip_lst = []     
# read keyword reporting 
keyword = pd.read_csv('/Users/april.liu/Documents/Search Term Report/Keyword report_Little Rock.csv',header=1,skiprows=0)


import re

# put all keywords in one list
keyword_list =[]
for row in keyword['Keyword']:
    row=row.split()
    keyword_list.append(row)

# remove + and space for each keyword and put them in one list
kwd_list = []
for a in keyword_list:
    for i in a:
        eachkwd = re.sub(r'[^\w]','',i).lower().strip()
        if eachkwd not in kwd_list:
            kwd_list.append(eachkwd)



# read search term reporting
df = pd.read_csv('/Users/april.liu/Documents/Search Term Report/Search term report_Little Rock.csv',header=1,skiprows=0)
df=df[:-1]

# put all search terms in one list
search_term_list = []
search_term = df[u'Search term']


for i in search_term:
    i = i.split()
    search_term_list.append(i)
 
# create empty dictinary for word_count frequency and total_impressions for each keyword

frequency = {}
total_impr = {}
for m in search_term_list:
    for n in m:
        if n not in frequency:
            frequency[n] = 1
        elif n in frequency:
            frequency[n] += 1
            
# create empty dictionary to only exlude those words which have existed in keyword_list
frequency_new = {k:v for k,v in frequency.items() if k not in kwd_list}

# convert impression column into list
I = df['Impressions']
impression_list = []
for j in I:
    impression_list.append(j)
    
# create list of tuples to store each word and each impression in each line
impressioneachword = []
for rownumber in range(len(impression_list)):
    for a in search_term_list[rownumber]:
        impressioneachword.append((a,impression_list[rownumber]))

# create total_impr dictionary to store each word and total impressions associated         
for item in impressioneachword:
    k,v = item
    if k not in total_impr:
        total_impr[k] = v
    elif k in total_impr:
        total_impr[k] += v
# create dictionary to store word and total impressions by excluding keywords that existed in keyword list
total_impr_new = {u:w for u,w in total_impr.items() if u not in kwd_list}

# create data frame to include word and frequency columns
df2 = pd.DataFrame(frequency_new.items(), columns = ('word','requency'))

# add total_impression column to data frame
df2['total_impr'] = [e for f,e in total_impr_new.items()]
df2 = df2.sort_values(by =['total_impr'],ascending=False)



# Create dictonary to store single word and the associated city name if existed
city_name = {}
for i in range(len(listing_info_list)):
    for x in frequency_new.keys():
        x = x.upper()
        if x in listing_info_list[i]:
            city_name.setdefault(x.lower(),[]).append(listing_info_lst[i])
zip_name = {}
for i in range(len(listing_info_list)):
    for x in frequency_new.keys():
        x = x.upper()
        if x in listing_info_list[i]:
            city_name.setdefault(x.lower(),[]).append(listing_info_lst[i])
            
df2['City'] = df2[u'word'].map(city_name) # create something like vlookup using python

df2.to_csv('/Users/april.liu/Documents/Search Term Report/search_term_frequency_Little Rock_6.3.16.csv', index=False)


