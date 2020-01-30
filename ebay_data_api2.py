from ebaysdk.shopping import Connection as shop
from bs4 import BeautifulSoup

ID_APP = 'YOUR EBAY DEVELOPERS APP-ID GOES HERE.'

Keywords = input('what are you searching for? \n')
api = shop(appid='BluntPro-LacROI-PRD-5d8d7989f-e1d12103', config_file=None)
api_request = { 'keywords': Keywords }
response = api.execute('FindPopularItems', api_request)
soup = BeautifulSoup(response.content,'lxml')

# totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')

for item in items:
    print(item)
    # cat = item.categoryname.string.lower()
    # title = item.title.string.lower()
    # price = int(round(float(item.currentprice.string)))
    # url = item.viewitemurl.string.lower()
    #
    # print('________---------------__________---------------____________')
    # print('cat:\n' + cat + '\n')
    # print('title:\n' + title + '\n')
    # print('price:\n' + str(price) + '\n')
    # print('url:\n' + url + '\n')