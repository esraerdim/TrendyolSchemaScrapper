import json
import bs4
import requests
from bs4 import BeautifulSoup
import lxml
import csv
import random
import time
data = []
deneme = []
errors = []
count = 0
random = random.randint(3,5)
with open('scraped_urls.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)


    for line in csv_reader:
          data.append(line)
    for row in data:
        url = row[0]
        try:
            r = requests.get(url)
            soup = bs4.BeautifulSoup(r.text, 'lxml')
            script_tag = soup.find("div", {"id": "product-detail-app"}).find('script')
            for script in script_tag:
                try:
                    data = json.loads(script)
                    deneme.append(data)
                    print("Success")
                    print(count, data)
                    with open('trendyolproduct.json','w')as json_file:
                        json.dump(deneme,json_file)
                except Exception:
                    print("Not Successful")

            time.sleep(random)
            count += 1
        except Exception:
            print(url)
            errors.append(url)
            with open('trendyol2.json','w') as not_success:
                json.dump(errors,not_success)
            continue







