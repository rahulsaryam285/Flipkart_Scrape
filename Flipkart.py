import requests
from bs4 import BeautifulSoup
import json
def flipkart():
    my_list=[]
    for i in range(1,11):
        url=requests.get("https://www.flipkart.com/search?q=mi+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mi+mobiles%7CMobiles&requestId=909bf62b-8732-4263-b254-99f1e36e37f8&as-searchtext=mi&page="+str(i)).text
        soup=BeautifulSoup(url,"html.parser")
        name=soup.find_all("div",class_="_4rR01T")
        name_list=[]
        for x in name:
            name_list.append(x.text)
        
        price=soup.find_all("div",class_="_30jeq3 _1_WHN1")
        price_list=[]
        for y in price:
            price_list.append(y.text[1:])

        rating=soup.find_all("div",class_="gUuXy-")
        rating_list=[]
        for z in rating:
            rating_list.append(z.text[:3])
        
        detail=soup.find_all("div",class_="fMghEO")
        detail_list=[]
        for x in detail:
            data=x.find_all("li",class_="rgWa7D")
            new_list=[]
            for y in data:
                new_list.append(y.text)
            detail_list.append(new_list)
       
        for j,k,l,m in zip(name_list,price_list,rating_list,detail_list):
            new_dict={}
            new_dict["Name"]=j
            new_dict["price"]=k
            new_dict["Rating"]=l
            new_dict["Details"]=m
            my_list.append(new_dict)
    return my_list
with open("Flipkart.json","w") as obj:
    json.dump(flipkart(),obj,indent=4)
