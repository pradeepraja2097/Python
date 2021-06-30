from bs4 import BeautifulSoup
import requests
import pandas as pd 
url="https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=6cd2b190-e977-40e5-b093-fdc0b5d96b06&as-searchtext=lap"
response=requests.get(url) #getting response from the url
print(response)
# Html content of that page
htmlcontent=response.content 
soup=BeautifulSoup(htmlcontent,"html.parser")
print(soup.prettify)
products=[]
prices=[]
for i in soup.find_all('a',href=True,attrs={'class':'_1fQZEK'}):
  try:
    product=i.find('div',attrs={'class':'_4rR01T'})
    price=i.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    products.append(product.text)
    prices.append(price.text)  
  except:
    print("exception")
print(len(products))
print(prices)
df=pd.DataFrame({'product Name':products,'prices':prices})
df.head()
df.to_csv('laptops')