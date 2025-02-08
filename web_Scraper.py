# start
# import two modules requests and BeautifulSoup
# select the site      ------- > you want  information from him 
# select this information On a body      ------ > (html) 
# and select where exist this information
# using select_one  method to locate the price 
# using p["class"][1] to locate the rate 
# using book.h3.a["title"] to locate the title 
# print this information to user 
# End 
import requests
from bs4 import BeautifulSoup

response =  requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.content,"html.parser")
books  = soup.find_all("article")
for book in books :
    price =  book.select_one("p.price_color")
    res = price.get_text()
    rate = book.p["class"][1]
    title =  book.h3.a["title"]
    print(f" this is a title {title} the rate is a {rate}  and this a price {res}" )
    

