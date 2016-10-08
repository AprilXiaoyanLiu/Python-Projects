# Python


This projects contains my random exercises with pandas module using Python

How to Process large csv file using python?

http://stackoverflow.com/questions/25962114/how-to-read-a-6-gb-csv-file-with-pandas
http://stackoverflow.com/questions/17444679/reading-a-huge-csv-in-python
http://stackoverflow.com/questions/27917760/removing-first-line-of-big-csv-file-in-python-v3


What's the difference between None and nan?
http://stackoverflow.com/questions/17534106/what-is-the-difference-between-nan-and-none
http://pandas-docs.github.io/pandas-docs-travis/

Edit values for subset of rows
http://stackoverflow.com/questions/13842088/set-value-for-particular-cell-in-pandas-dataframe

errors 'UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 10: ordinal not in range(128)' when saving to excel pandas
http://stackoverflow.com/questions/33940319/issue-saving-data-in-excel

How to merge two lists into a list of tuple?
http://stackoverflow.com/questions/2407398/python-merge-items-of-two-lists-into-a-list-of-tuples

How to capitalize the first letter of each word in a string (Python)?


http://stackoverflow.com/questions/10017147/removing-a-list-of-characters-in-string
http://stackoverflow.com/questions/1549641/how-to-capitalize-the-first-letter-of-each-word-in-a-string-python


http://stackoverflow.com/questions/21702342/creating-a-new-column-based-on-if-elif-else-condition

next() list iterator
http://stackoverflow.com/questions/16814984/python-list-iterator-behavior-and-nextiterator

http://stackoverflow.com/questions/19384532/how-to-count-number-of-rows-in-a-group-in-pandas-group-by-object

http://stackoverflow.com/questions/26336251/pandas-rename-single-dataframe-column-without-knowing-column-name

how to add datetime to the filename:

http://stackoverflow.com/questions/17465045/can-pandas-automatically-recognize-dates

from datetime import datetime

filename = '/path/to/output/myfile-%s.txt'%datetime.now().strftime('%Y-%m-%d')

http://stackoverflow.com/questions/23377108/pandas-percentage-of-total-with-groupby

http://stackoverflow.com/questions/15705630/python-getting-the-row-which-has-the-max-value-in-groups-using-groupby

choose the top N within subgroups

http://stackoverflow.com/questions/20069009/pandas-good-approach-to-get-top-n-records-within-each-grouphttp://stackoverflow.com/questions/17465045/can-pandas-automatically-recognize-dates

choose top n rows within each subgroup - redshift

http://stackoverflow.com/questions/1124603/grouped-limit-in-postgresql-show-the-first-n-rows-for-each-group

http://stackoverflow.com/questions/17465045/can-pandas-automatically-recognize-dates

How to get time of a python program execution

http://stackoverflow.com/questions/1557571/how-to-get-time-of-a-python-program-execution


http://stackoverflow.com/questions/10017147/removing-a-list-of-characters-in-string

http://stackoverflow.com/questions/6116978/python-replace-multiple-strings

http://stackoverflow.com/questions/17134716/convert-dataframe-column-type-from-string-to-datetime

http://stackoverflow.com/questions/17749484/python-script-to-concatenate-all-the-files-in-the-directory-into-one-file

http://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe

http://stackoverflow.com/questions/16353729/pandas-how-to-use-apply-function-to-multiple-columns

how to randomly choose data

import random

unique_users = test.user_id.unique()

sel_user_ids = [unique_users[i] for i in sorted(random.sample(range(len(unique_users)), 10000)) ]
sel_test = test[test.user_id.isin(sel_user_ids)]


#Web Scraping
http://www.diveintopython.net/http_web_services/redirects.html

http://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautifulsoup


