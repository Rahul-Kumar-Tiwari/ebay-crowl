import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
import csv
import time


#url = 'https://www.ebay.com/sch/dailyrefinement/m.html?_nkw=&_armrs=1&_ipg=&_from=&rt=nc&LH_BIN=1'
url=str(input("Please enter main store link: "))
page_link=[url,]
item=[]
key=1
datamain=[["Title of Product","Link of Product",'Item No of Ebay','Description','Condition','Price','Dict Data Multifield','image','Shipping Charge','Courier','Return Policy'],]


def item_link_crowl(weburl):
        time.sleep(5)
        url = weburl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class': 'vip'}):
                tet_2 = link.get('href')
                item.append(tet_2)
                print(tet_2)

def item_description_crowling(weburl):
        time.sleep(5)
        data=[]
        url = weburl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        # Title of product
        for heading in s.findAll('h1',{'class':'it-ttl'}):
                a = BeautifulSoup(str(heading))
                [x.extract() for x in a.findAll('span')]
                data.append(a.text)
                print(a.text)
        data.append(url)

        for item_number in s.findAll('div',{'class':'u-flL iti-act-num itm-num-txt'}):
                data.append(item_number.text)
                print("item No : ",item_number.text)

        # # description of product
        for desc_link in s.findAll('iframe', {'id': 'desc_ifr'}):
                des_link=desc_link.get('src')
                code = requests.get(des_link)
                plain = code.text
                sub = BeautifulSoup(plain, "html.parser")
                for desc in sub.findAll('div', {'id': 'ds_div'}):
                        a = BeautifulSoup(str(desc))
                        [x.extract() for x in a.findAll('style')]
                        data.append(a.text)
                        print(a.text)
        # #condition of product
        for div in s.findAll('div', {'id': 'vi-itm-cond','class':'u-flL condText'}):
                data.append(div.text)
                print(div.text)
        # # #Price of product
        for div in s.findAll('div', {'class':'mm-op u-flL'}):
                data.append(div.contents[2].text)
                print(div.text)

        # product details
        dict={}
        for div in s.findAll('div', {'class': 'section'}):
                table = div.find("table", {"role": "presentation"})
                rows = table.find_all('tr')
                for row in rows:
                        cols = row.find_all('td')
                        i=0
                        sort=[]
                        for col in cols:
                                i=i+1
                                column=col.text.replace('\n','')
                                column=column.replace('\t','')
                                column=column.split(':')
                                sort.append(column[0])
                                if i==2:
                                        dict[sort[0]]=sort[1]
                                        i=0
                                        sort=[]
        print(dict)
        data.append(dict)
        #image
        image=''
        for td in s.findAll('td', {'class': 'tdThumb'}):
                for div in td.findAll('div'):
                        for img in div.findAll('img'):
                                image_name=img.get('src')
                                image_name=image_name.replace("l64.jpg",'l300.jpg')
                                image=image+","+image_name

        print(image)
        data.append(image)
        #shiping Charge
        for shipping in s.findAll('div',{'class':'u-flL sh-col'}):
                for ship in shipping.findAll('span',{'id':'fshippingCost'}):
                        a = BeautifulSoup(str(ship))
                        [x.extract() for x in a.findAll('span',{'class':'sh-svc sh-nwr'})]
                        data.append(a.text)


        #courier
        for courier in s.findAll('span', {'id': 'fShippingSvc'}):
                data.append(courier.text)
                print(courier.text)

        #Return Policy
        for ret_policy in s.findAll('span', {'id': 'vi-ret-accrd-txt'}):
                data.append(ret_policy.text)
                print(ret_policy.text)

        datamain.append(data)


def next_page(url1):
        global key,url
        code = requests.get(url1)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        try:
                for tdata in s.findAll('td', {'class':'pagn-next'}):
                        link=tdata.find('a', {'class':'gspr next'})
                        if link:
                                tet_2 = link.get('href')
                                page_link.append(tet_2)
                                url=tet_2
                                print(url)
                        else:
                                key=0
        except:
                key=0


# while(key!=0):
#         next_page(url)
# print('Page length---->',len(page_link))
# for link in page_link:
#         item_link_crowl(link)
# print("Item---->",len(item))
# for item_link in item:
#         item_description_crowling(item_link)
# with open('Data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(datamain)


item_link_crowl('https://www.ebay.com/sch/dailyrefinement/m.html?_nkw=&_armrs=1&_ipg=&_from=&rt=nc&LH_BIN=1')
for item_link in item:
         item_description_crowling(item_link)
with open('Data.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerows(datamain)