from requests import get
from bs4 import BeautifulSoup
import csv

#statics
city = 'poznan'
olx_base_url = 'https://www.olx.pl'
olx_url = '{0}/nieruchomosci/stancje-pokoje/{1}/?view=list'.format(olx_base_url, city)
file_name = 'olx_room_data.csv'

#get data from website
response = get(olx_url)
html_soup = BeautifulSoup(response.text, 'html.parser')

#find all offers on page & get links
offer_containers = html_soup.find_all('div', class_='offer-wrapper')
offer_urls = []

for offer in offer_containers:
    offer_url = offer.find('a', href=True)
    offer_urls.append(offer_url['href'])

#initialize offer list
offer_list = []

#process offer
for idx, url in enumerate(offer_urls):
    # check if not an advertisement
    if(olx_base_url not in url):
        continue

    # get offer page
    response = get(url)
    offer_soup = BeautifulSoup(response.text, 'html.parser')

    # scrap data
    offer_dict = {} 
    location = offer_soup.find('a', class_='show-map-link').getText().split(',')
    offer_dict['city'] = location[0]
    offer_dict['region'] = location[1]
    offer_dict['district'] = location[2]
    offer_dict['price'] = offer_soup.find('div', class_='price-label').getText().strip('\n')
    
    raw_html_description = offer_soup.find('div', {'id': 'textContent', 'class': 'clr'}).getText()
    offer_dict['description'] = "".join(line.strip() for line in raw_html_description.split('\n'))

    # parse data in table
    all_values_from_table = offer_soup.find_all('td', class_='value')
    for val in all_values_from_table:
        offer_dict[val.parent.find('th').getText()] = val.getText().split()

    # save to list
    offer_list.append(offer_dict)
    print("Processing offer no {0}".format(str(idx + 1)))


# save to file
keys = ['city', 'region', 'district', 'price', 'Oferta od', 'Umeblowane', 'Rodzaj pokoju', 'Preferowani', 'description']

with open('olx_room_data.csv', 'w', newline='', encoding='utf-16') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(offer_list)