import pandas as pd
import numpy as np 
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
headers = {"Accept-Language": "en-US,en;q=0.5"}
movie_name=[]
year=[]
time=[]
rating=[]
metascore=[]
votes=[]
gross=[]

pages=np.arange(1,1000,100)

for page in pages:
    page= requests.get("https://www.goodreads.com/genres/romance")
    soup=BeautifulSoup(page.text,"html.parser")
    movie_data=soup.find_all('tr',attrs={'itemtype':'http://schema.org/Book'})
    sleep(randint(2,8))
    for store in movie_data:
        name = store.td.tr.text
        movie_name.append(name)
    print(movie_name)

