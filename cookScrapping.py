import requests
from selenium import webdriver 
import pandas as pd
from bs4 import BeautifulSoup
name=[]
publish=[]
rating=[]
returnp=[]
author=[]
rate=[]
delivery=[]
for ur in range(1,50):
    url = 'https://www.amazon.com/s?k=cookbooks&page='+str(ur)+'&crid=3RGPIK8JR1LDH&qid=1666071865&sprefix=cookbook%2Caps%2C294&ref=sr_pg_'+str(ur)
    driv = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver.exe')
    driv.get(url)
    context=driv.page_source
    soup= BeautifulSoup(context,'html.parser')
    d=soup.findAll("div",class_='s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border')
    for i in d:
        try:
            pr1=(i.find('span',class_='a-price-whole').text)
            pr2=(i.find('span',class_='a-price-fraction').text)
            total=pr1+pr2
            rate.append(total)
        except:
            rate.append('0.00')
        try:
            rating.append(i.find('span',class_='a-size-base s-underline-text').text)
            
        except:
            rating.append('0')
        try:
            author.append(i.find('a',class_='a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style').text)
            
        except:
            author.append('Author Not found')
        ur=i.find('a',class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal').attrs["href"]
        newurl='https://amazon.com/'+ur
        driv.get(newurl)
        context=driv.page_source
        soup= BeautifulSoup(context,'html.parser')
        bokDetail=soup.findAll("div",class_='a-container')
        for b in bokDetail:
            try:
                name.append(b.find('span',attrs={'class':'a-size-extra-large'}).text)
            except:
                name.append('Name not founded')
            try:
                publish.append(b.find('span',attrs={'class':'a-size-large a-color-secondary'}).text)
            except:
                publish.append('Publish Date not founded')
            try:
                deli=b.findAll('div',class_='a-section')
                for dd in deli:
                    try:
                        delivery.append('span',attrs={"class":'a-text-bold'}).text
                    except:
                        delivery.append('delivery date not founded')
                    try:
                        returnp.append(dd.find('a',attrs={"id":'productSupportAndReturnPolicy-return-policy-anchor-text'}).text)
                    except:
                        returnp.append('no return policy ')                        
                    break
            except:
                print('Not Founded')
        pf=pd.DataFrame({"Publish Date":publish,"deliver Date":delivery,"return ":returnp,"Book Name":name,"Author Name":author,"Raitng":rating,"Price":rate,})
        pf.to_csv('cookData.csv',index=False,mode='w')