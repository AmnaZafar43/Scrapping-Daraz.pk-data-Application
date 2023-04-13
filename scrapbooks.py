import requests
from bs4 import BeautifulSoup
response= requests.get("https://www.alibris.com/search/books/subject/Fiction")
webpage = response.content
print(response.status_code)
soup = BeautifulSoup(webpage,"html.parser")
#the logic

for parent in soup.find_all('ul',class_="primaryList"):
    for n,tag in enumerate(parent.find_all('li')):
        title=[x for x in tag.find_all('p',class_="bookTitle")]
        auther=[x for x in tag.find_all('p',class_="author")]
        price=[x for x in tag.find_all('p',class_="buy")]
        for item in title:
            print("BOOK NAME:",item.text.strip())
        for item in author:
            author= item.text.split("\n")
            print("Author:",author[2])
        for item in price:
            print("PRICE:",item.text.strip())
        print()