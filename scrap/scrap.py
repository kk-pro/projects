# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
import bs4
import re

# %%
l=[]
base_url="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="

for page in range(0, int(page_n)*10,10):
    r=requests.get(base_url+str(page)+".html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    for item in all:
        d={}
    
        d["Adress"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
        try:
            d["Locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
        except:
            d["Locality"]=None

        d["Price"]=item.find("h4",{"class","propPrice"}).text.replace("\n","").replace(" ","")
        try:
            d["Bed"]=item.find("span",{"class":"infoBed"}).find("b").text
        except:
            d["Bed"]=None
        try:
            d["Bath"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            d["Bath"]=None
        l.append(d)    


# %%
l


# %%
import pandas
df=pandas.DataFrame(l)


# %%
df


# %%
df.to_csv("Output.csv")


# %%



