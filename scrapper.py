
import json
import csv
import requests
from bs4 import BeautifulSoup

url="http://books.toscrape.com"

def scrape_books(url):
    response=requests.get(url)
    if response.status_code != 200:
        print("cannot fetch data")
        return
    
    response.encoding = response.apparent_encoding#set encoding explicity to handle special characters
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="product_pod")
    books=[]
    for article in articles:
        title = article.h3.a['title']
        print(title)
        price_text = article.find("p", class_="price_color").text
        print(price_text)
        currency = price_text[0]
        price = float(price_text[1:])
        print(title,currency,price)
        
        
        books.append({
            "title": title,
            "currency": currency,
            "price": price
        })
    return books


all_books = scrape_books(url,) 
if all_books:
    with open("books.csv", "w",newline="", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=all_books[0].keys())
        writer.writeheader()
        writer.writerows(all_books)
    print("Data written to books.csv")
 
with open("books.json", "w", encoding="utf-8") as f:
    json.dump(all_books,f, indent=2, ensure_ascii=False )#ensure_ascii=False not to escape non ascii character
# git config --global user.email "kreepakhanal1@gmail.com"
#f#b#qgit 
