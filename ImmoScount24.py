from bs4 import BeautifulSoup
import requests
import csv

url = ('https://www.immoscout24.ch/en/flat/rent/canton-zug')
current_page = 1

immo_file = open('ImmoScount24.csv', 'w', encoding='utf-8') #this encoding helps with strange characters
immo_writer = csv.writer(immo_file)
immo_writer.writerow(['Describtion', 'Rooms', 'Size', 'Price', 'Location', 'Link'])

og_source = requests.get(url + '?pn=' + str(current_page))
og_soup = BeautifulSoup(og_source.text, 'lxml')

total_pages = og_soup.find_all(class_="sc-htoDjs fsjvuy")[-1].text
int_total_pages = int(total_pages)

while current_page <= int_total_pages:

    source = requests.get(url + '?pn=' + str(current_page))
    soup = BeautifulSoup(source.text, 'lxml')

    house = soup.find_all(class_="sc-dUjcNx dttIeR")
    link = soup.find_all(class_='a class="sc-dHmInP cqorGi')

    for i in house:

        try:
            describtion = i.h2.get_text().replace('Â«','').replace('Â»','').replace('Ã¶', 'ö').replace('Ã¼', 'ü').replace('Ã¤', 'ä')
        except:
            describtion = None

        try:
            rooms = i.h3.get_text().replace('Â', '').replace('â', '-').split(',')[0]
        except:
            rooms = None

        try:
            size = i.h3.get_text().replace('Â', '').replace('â', '-').split(',')[1]
        except:
            size = None

        try:
            price = i.find(class_='sc-kbdWBx dFFQWL sc-eAyhxF hEftah')
        except:
            price = None

        try:
            location = i.find(class_='sc-dHmInP lgslPl')
        except:
            location = None

        try:
            link = i.find('a', href=True)
            only_link = link['href']
            immo_link = f'https://www.immoscout24.ch{only_link}'
        except:
            link = None

        immo_writer.writerow([describtion, rooms, size, price.text, location.text, immo_link])

    current_page += 1

immo_file.close()

