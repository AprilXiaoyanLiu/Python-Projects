# -*- coding: utf-8 -*-
"""
Spyder Editor
command spyder
This is a temporary script file.
"""

import pandas as pd


# read keyword reporting 
keyword = pd.read_csv('/Users/April/Keyword report_c.csv',header=1,skiprows=0)
# delete the last two rows since they are total numbers
keyword = keyword[:-2]

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
df = pd.read_csv('/Users/April/Search term report.csv',header=1,skiprows=0)
df=df[:-1]

# put all search terms in one list
search_term_list = []
search_term = df['Search term']
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
df2 = df2.sort(['total_impr'],ascending=False)
# write dataframe to csv
df2.to_csv('/Users/April/search_term_frequency_cincinnatti.csv', index=False)








    
