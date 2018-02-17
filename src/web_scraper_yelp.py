import os
import sys
import requests
import csv
import re
import time
from bs4 import BeautifulSoup

# Scrapes all resturants for Pittsburgh by sending requests to Yelp API
def yelp():
    api = "cN5rYNCY5_xo17rpYiobB4zvkMfJg6P8myaszdQpkyh16Fo49_jFVSOIicwh2SB_MP7dUi_YvwnDpBHwMygewpfwAP-ucFytRt1d78iL_0ddLsgmE7LcpOsGfGNxWnYx"
    headers = {"authorization": 'Bearer %s' % api}
    params = {"location": "Pittsburgh", "categories" : "restaurants"}
    response = requests.get('https://api.yelp.com/v3/businesses/search', headers=headers, params=params)
    result = response.json() 
    content = 'Name,Rating,Review_Count,Price,Cuisine,Latitude,Longitude,Street,City,Zip'
    total = result['total']
    for i in range(0, total, 20):
        time.sleep(0.25)
        params = {"location": "Pittsburgh", "categories" : "restaurants", "offset" : i}
        response = requests.get('https://api.yelp.com/v3/businesses/search', headers=headers, params=params)
        result = response.json()
        if 'businesses' in result:
            for restaurant in result['businesses']:
                content += '\n' + restaurant['name'] + ',' + str(restaurant['rating']) + ',' + str(restaurant['review_count']) + ','
                if 'price' not in restaurant:
                    price = ''
                else:
                    price = restaurant['price']
                content +=  price + ',' + restaurant['categories'][0]['title'] + ',' + str(restaurant['coordinates']['latitude']) + ',' + str(restaurant['coordinates']['longitude']) + ','+ ','.join(restaurant['location']['display_address'])
    # Writing to CSV file
    f = open(os.path.join("yelp.csv"), 'w', encoding='utf8' )
    f.write(content)
    f.close()

# main driver
if __name__ == "__main__":
   os.chdir(os.path.dirname(sys.argv[0]))
   yelp()


