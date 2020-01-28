from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

ID_APP = 'YOUR EBAY DEVELOPERS APP-ID GOES HERE.'

Keywords = input('what are you searching for? \n')
api = finding(appid='RahulKum-Hamock-PRD-dca83364c-ae99eac8', config_file=None)
api_request = { 'keywords': Keywords }
response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content,'lxml')

totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')

for item in items:
    cat = item.categoryname.string.lower()
    title = item.title.string.lower()
    price = int(round(float(item.currentprice.string)))
    url = item.viewitemurl.string.lower()

    print('________')
    print('cat:\n' + cat + '\n')
    print('title:\n' + title + '\n')
    print('price:\n' + str(price) + '\n')
    print('url:\n' + url + '\n')
    input()