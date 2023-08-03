import requests
from bs4 import BeautifulSoup
import re

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)

# # print(r.text)
#
# soup=BeautifulSoup(r.text,"lxml")
# # print(soup.div.ul)
# tag=soup.header
# atb=tag.attrs
# # print(tag.attrs)
# # print(atb["role"])
# # print(soup.div.p)
# # print(soup.div.p.string)
# print(soup.header.p)

# print(r)
soup=BeautifulSoup(r.text,"lxml")

# price=(soup.find("h4",{"class":"pull-right price"}))
# print(price.string)


# desc=(soup.find("p",{"class":"description"}))
# print(desc.string)

# desc=(soup.find("p",class_="description"))
# print(desc.string)

# prices=(soup.findAll("h4",class_="pull-right price"))

# print(len(prices))
# for i in prices:
#     print(i.text)

# print(prices[3])

# desc=soup.findAll("p",class_="description")
# print((desc[3]).string)

# data=soup.findAll(["a","p"])
# print(data)

# data=soup.findAll(string="Galaxy Tab")
# print(data)

# data=soup.find_all(string=re.compile("Galaxy"))
# print(data)

import pandas as pd

names=soup.findAll("a",class_="title")
# print(names)
product_names=[]
for i in names:
    name=i.text
    product_names.append(name)

# print(product_names)


prices=soup.findAll("h4",class_="pull-right price")
prices_list=[]
for i in prices:
    prices=i.text
    prices_list.append(prices)

# print(prices_list)

desc=soup.findAll("p",class_="description")
desc_list=[]
for i in desc:
    desc=i.text
    desc_list.append(desc)

# print(desc_list)

reviews=soup.findAll("p",class_="pull-right")
reviews_list=[]
for i in reviews:
    temp=i.text
    reviews_list.append(temp)
# print(reviews_list)

df=pd.DataFrame({"Product Name": product_names,"Prices": prices,"Descritpion":desc_list,"reviews":reviews_list})
# print(df)
df.to_csv(r"C:\Users\user\Downloads\productlist.csv")
