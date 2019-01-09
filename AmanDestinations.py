from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.aman.com/destinations')
soup = BeautifulSoup(source.text, 'lxml')

aman = soup.find_all(class_='destinations-text views-fieldset')

csv_file = open('AmanDestinations.csv', 'w') # the 'w' stands for write

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Destination', 'Text', 'Resort'])

for i in aman:
    destination = i.h3.get_text()
    text = i.p.get_text()
    resort = i.find(class_='btn-wrapper').get_text()

    csv_writer.writerow([destination, text, resort])

csv_file.close()













