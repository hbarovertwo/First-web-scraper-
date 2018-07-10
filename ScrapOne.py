"""
Created by Mason Christensen
July 10th 2018
First web scrape project with python using requests and BeautifulSoup
"""

import requests
from bs4 import BeautifulSoup

#connect to the best seller page
n = requests.get("https://www.amazon.com/Best-Sellers/zgbs")

#Parse the raw html
soup = BeautifulSoup(n.text, 'html.parser')

#After observing product names and ratings from HTML, pull that data
prn = soup.find_all('a', attrs = {'class':'a-link-normal'})

#Pull the names, ratings, number of ratings from within tags
for a in range(0,len(prn)):
    prn[a] = prn[a].text.strip()

#display data as a drop down list.
print("Below are the top 3 best sellers of each major amazon category, followed by rating and number of ratings if available.")
for a in range(0,len(prn)):
    print(str(a) + ' ' + prn[a])

