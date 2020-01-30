import requests
search=input('what are you searching for? \n')
limit=input('Search limit??\n')

url = 'https://api.ebay.com/buy/browse/v1/item_summary/search?q='+search+'&limit='+limit

headers = {
    "Authorization":"Bearer v^1.1#i^1#p^3#I^3#f^0#r^0#t^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",
    "X-EBAY-C-MARKETPLACE-ID": "EBAY_US",
    # " Content-Type " : "application/json"
    "Content-Type": "application/json",
    # "X-EBAY-C-ENDUSERCTX":contextualLocation=country=<2CharCountryCode>,zip=<5DigitCode>,affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>
    # "X-EBAY-API-COMPATIBILITY-LEVEL": 851,
    # "X-EBAY-API-DEV-NAME": "673129be-95fe-4e8e-84af-dc8293756263",
    # "X-EBAY-API-APP-NAME": "BluntPro-LacROI-PRD-5d8d7989f-e1d12103",
    # "X-EBAY-API-CERT-NAME": "PRD-d8d7989fbf9c-4f5b-4753-8e6d-6e33",

}

req = requests.get(url,headers=headers)
print(req.status_code)
r_json=req.json()
print(r_json)
items=r_json['itemSummaries']
item_id=[]
for item in items:
    print(item)
    itemId=item['itemId']
    item_id.append(itemId)
    print(itemId)
    title=item['title']
    print(title)
    image=item['image']['imageUrl']
    print(image)
    price=item['price']["value"]
    print(price)
    currency=item['price']['currency']
    print(currency)
    seller_name=item['seller']['username']
    print(seller_name)
    condition=item['condition']
    print(condition)
    shipping_cost=item['shippingOptions']
    for ship in shipping_cost:
        print(ship['shippingCostType'])
        print(ship['shippingCost']['value'])
        print(ship['shippingCost']['currency'])
    # itemAffiliateWebUrl=item['itemAffiliateWebUrl']
    # print(itemAffiliateWebUrl)
    itemWebUrl=item['itemWebUrl']
    print(itemWebUrl)

    img = ''
    try:
        additionalImages=item['additionalImages']
        for add_image in additionalImages:
            img=img+","+str(add_image['imageUrl'])
    except:
        img="Aditional Image not found"
    print(img)
for get_item in item_id:
    url1='https://api.ebay.com/buy/browse/v1/item/'+get_item
    req = requests.get(url1, headers=headers)
    print(req.status_code)
    r_json = req.json()
    print(r_json)
