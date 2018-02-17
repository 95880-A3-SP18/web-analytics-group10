import os
import sys
import requests
import csv
import time

def download_data():
   r = requests.get('https://developers.zomato.com/api/v2.1/search?entity_id=1081&entity_type=city&sort=rating&order=desc', headers={'user-key' : '2a1c6f3bcec19c6ae981419cb5df1bc0'})
   if r.status_code != 200:
      return 
   total_count = r.json()['results_found']
   count = total_count / 20

   ofile  = open('/Users/devsen/Desktop/downloads' + '/links_zomato.csv', "w")
   wr = csv.writer(ofile, quoting=csv.QUOTE_ALL)

   wr.writerow(['Name', 'Address', 'Locality', 'City', 'Zip', 'lat', 'lon', 'Cuisines', 'Rating', 'Rating text', 'Votes'])

   i = 0
   start = 0
   while i < count:
      r = requests.get('https://developers.zomato.com/api/v2.1/search?entity_id=1081&entity_type=city&start=' + str(start) + '&sort=rating&order=desc', headers={'user-key' : '2a1c6f3bcec19c6ae981419cb5df1bc0'})
      time.sleep(0.3)
      write_data(wr, r.json()['restaurants'])
      i += 1
      start += 20


def write_data(wr, data):
   for json in data:
      j = json['restaurant']
      row = []
      row.append(j['name'])
      location = j['location']
      row.append(location['address'])
      row.append(location['locality'])
      row.append(location['city'])
      row.append(location['zipcode'])
      row.append(location['latitude'])
      row.append(location['longitude'])
      row.append(j['cuisines'])
      rating = j['user_rating']
      row.append(rating['aggregate_rating'])
      row.append(rating['rating_text'])
      row.append(rating['votes'])
      wr.writerow(row)


if __name__ == "__main__":
   os.chdir(os.path.dirname(sys.argv[0]))
   download_data()
