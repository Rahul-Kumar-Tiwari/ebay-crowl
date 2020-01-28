from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
import csv

ID_APP = 'YOUR EBAY DEVELOPERS APP-ID GOES HERE.'

Keywords = input('what are you searching for? \n')
api = finding(appid='RahulKum-Hamock-PRD-dca83364c-ae99eac8', config_file=None)
api_request = { 'keywords': Keywords }
response = api.execute('findItemsByKeywords', api_request)
print(response)
soup = BeautifulSoup(response.content,'lxml')
print(soup)

totalentries = int(soup.find('totalentries').text)
print("totalentries",totalentries)
items = soup.find_all('item')
print(len(items))
datamain=[['category','Title','Price','Url','id','subtitle','Galleryurl','Payment Method','Postal Code','Location','country',
            'shippingservicecost','shippingtype','expeditedshipping','conditiondisplayname','sellingstate',
           'returnsaccepted','ismultivariationlisting','originalretailprice'],]
for item in items:
    data=[]
    try:
        category = item.categoryname.string.lower()
        title = item.title.string.lower()
        price = int(round(float(item.currentprice.string)))
        url = item.viewitemurl.string.lower()
        id=int(item.itemid.string)
        subtitle=item.subtitle.string.lower()
        galleryurl=item.galleryurl.string.lower()
        payment_method=item.paymentmethod.string.lower()
        postal_code=item.postalcode.string.lower()
        location=item.location.string.lower()
        country=item.country.string.lower()
        shippingservicecost=item.shippingservicecost.string.lower()
        shippingtype=item.shippingtype.string.lower()
        expeditedshipping=item.expeditedshipping.string.lower()
        conditiondisplayname=item.conditiondisplayname.string.lower()
        sellingstate=item.sellingstate.string.lower()
        returnsaccepted=item.returnsaccepted.string.lower()
        ismultivariationlisting=item.ismultivariationlisting.string.lower()
        originalretailprice=int(round(float(item.originalretailprice.string)))

        print(
            '--------------------------------------------------------------------------------------------------------')
        data.append(category)
        # print('category: ' + category)
        data.append(title)
        # print('title: ' + title)
        data.append(str(price))
        # print('price: ' + str(price))
        data.append(url)
        # print('url: ' + url)
        data.append(id)
        # print('Id: ', id)
        data.append(subtitle)
        # print("subtitle: ", subtitle)
        data.append(galleryurl)
        # print("galleryurl :", galleryurl)
        data.append(payment_method)
        # print('payment_method: ', payment_method)
        data.append(postal_code)
        # print('postal_code: ',postal_code)
        data.append(location)
        # print('location: ', location)
        data.append(country)
        # print("country: ", country)
        data.append(shippingservicecost)
        # print('shippingservicecost: ', shippingservicecost)
        data.append(shippingtype)
        # print('shippingtype: ', shippingtype)
        data.append(expeditedshipping)
        # print('expeditedshipping :', expeditedshipping)
        data.append(conditiondisplayname)
        # print('conditiondisplayname: ', conditiondisplayname)
        data.append(sellingstate)
        # print('sellingstate: ', sellingstate)
        data.append(returnsaccepted)
        # print('returnsaccepted: ', returnsaccepted)
        data.append(ismultivariationlisting)
        # print('ismultivariationlisting: ', ismultivariationlisting)
        data.append(originalretailprice)
        # print('originalretailprice: ',originalretailprice)
        datamain.append(data)
    except:
        print("*********something Missing in this Data**********")
        print(item)
with open('Data_Search_api.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(datamain)






    # input()