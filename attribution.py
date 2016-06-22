# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:35:14 2016

@author: april.liu
"""

import pandas as pd
from sqlalchemy import create_engine

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import plotly.plotly as py
import numpy as np



# Create Connection Engines to Stingray and Redshift 
engine_RS = create_engine('postgresql://april.liu:VVUamGKs71@10.0.7.23:5439/rmus_prod') 

#
Counts_Query = '''select login_id, count(*) as counts from

(select a.request_timestamp, a.event_category, a.event_type, a.querystring, a.login_id, b.first_contact_date
from edw.marketing_event a right join (select distinct login_id, first_value(contact_date) 
over (partition by login_id order by contact_date asc
rows between unbounded preceding and unbounded following) as first_contact_date
from edw.login_contact) b on a.login_id = b.login_id
where request_timestamp < first_contact_date and querystring not like '%%utm_source=myredfin%%')

group by login_id
having count(*) < 50
order by count(*) desc'''

touchpoints_dataframe = pd.read_sql(Counts_Query, con = engine_RS)

# understand counts of touchpoints distribution

counts_table = touchpoints_dataframe['counts'].value_counts()
counts_dataframe = pd.DataFrame(counts_table, columns = ['counts'])
counts_dataframe['cum_sum'] = counts_dataframe.counts.cumsum()
counts_dataframe['cum_perc'] = counts_dataframe.cum_sum/np.sum(counts_dataframe['counts'])
print counts_dataframe

'''
hist, bin_edges = np.histogram(counts_table, normed=True)
print bin_edges
print hist
print np.cumsum(hist)'''

# fequency histogram
plt.hist(touchpoints_dataframe['counts'])
plt.title("Touchpoints Frequency")
plt.xlabel("counts")
plt.ylabel("frequency")
plt.show()

# CDP Graph
num_bins = 50
mu = np.mean(touchpoints_dataframe['counts'])
sigma = np.std(touchpoints_dataframe['counts'])

n, bins, patches = plt.hist(touchpoints_dataframe['counts'], num_bins, normed=1, facecolor = 'green', alpha = 0.5, histtype='step', cumulative=True)
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Counts')
plt.ylabel('Probability')
plt.show()

# density histogram
num_bins = 50
mu = np.mean(touchpoints_dataframe['counts'])
sigma = np.std(touchpoints_dataframe['counts'])
# histogram of data; cumulative of data
n, bins, patches = plt.hist(touchpoints_dataframe['counts'], num_bins, normed=1, facecolor = 'green', alpha = 0.5)
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Counts')
plt.ylabel('Probability')
plt.show()


