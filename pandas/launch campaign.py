# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:53:14 2016

@author: April
"""

# read specific sheet in excel and create listing pivot table
import pandas as pd
import numpy as np
excel = pd.ExcelFile('/Users/April/Downloads/Google Geo-Gen For Sale Atlanta.xlsm' )
df = excel.parse('Listing Data')
listing_pivot = pd.pivot_table(df,values = 'count',index = ['upper'], columns = ['property_type'],aggfunc=np.sum).reset_index()
print listing_pivot.sort(['Single Family Residential'], ascending=[False])
grouped =  df.groupby('upper').sum().reset_index()




listing_info =  grouped[['upper','count']].sort().sort(['count'], ascending=False)
listing_info['percent'] = [100.00*x/listing_info['count'].sum() for x in listing_info['count']]
listing_info['cum_percent'] = listing_info['count'].cumsum()/listing_info['count'].sum()

select_city = listing_info.loc[listing_info['cum_percent'] <= 0.5]

city_name = [x+',GA' for x in select_city['upper']]

print city_name

# extract listing cities lat lng 
import geocoder
g = geocoder.google('Atlanta,GA')


city_name_list = []
for m in city_name:
    m.encode('utf=8')
    g = geocoder.google(m)
    city_name_list.append(g)

city_name_list
    

# check if it is within polygon


from shapely.geometry import Point, Polygon
pt = Point(0.75, 0.25)
poly = Polygon([(0,0),(1,1),(1,0)])



# write to excel 

writer = pd.ExcelWriter(r'c:\file.xlsx', engine = 'xlsxwriter')
workbook - writer.book
df.to_excel(writer, index=True, sheet_name ='Sheet1')

startrow : upper left cell row to dump data frame

startcol : upper left cell column to dump data frame
