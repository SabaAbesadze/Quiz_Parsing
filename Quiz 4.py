import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

payloads = {'cids': 105569, 'p': 1}
url = 'https://ge.iherb.com/new-products'
h = {'Accept-Language': 'en-US'}
file = open('Iherb.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['Description', 'Price'])

while payloads['p'] < 7:
    response = requests.get(url, params=payloads, headers=h)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    Iherbs_soup = soup.find('div', class_='products product-cells clearfix')
    all_Iherbs = Iherbs_soup.find_all('div', class_='product-cell-container col-xs-12 col-sm-12 col-md-8 col-lg-6')
    for Iherb in all_Iherbs:
        Description = Iherb.find('div', class_='product-title').bdi.text
        Price = Iherb.find('span', class_='price').bdi.text
        print(Description, Price)
        csv_obj.writerow([Description, Price])
    payloads['p'] += 1
    sleep(randint(7, 16))

file.close()
