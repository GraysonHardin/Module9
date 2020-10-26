"""
Program: scraper.py
Author: Grayson Hardin
Last date modified: 10/26/2020

This program takes a url package and prints off the results. It does not look the best, but the Soup import helps sort it. Additionally, it writes to the console as well.
"""
import requests
from bs4 import BeautifulSoup

url = 'https://dmacc.edu/Schedule/Pages/welcome.aspx'
response = requests.get(url)
html = response.content
f = open("requestResult.txt", "w+")
f.writelines(str(html))
f.close()

soup = BeautifulSoup(open("requestResult.txt"), 'html.parser')
print(soup.prettify())


