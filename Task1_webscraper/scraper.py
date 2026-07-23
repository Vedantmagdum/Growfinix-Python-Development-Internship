import requests
from bs4 import BeautifulSoup
import csv

url = "http://127.0.0.1:5500/property_listings.html"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

properties = soup.find_all("div", class_="property-card")

with open("property_listings.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Title", "Price", "Location"])

    for property in properties:

        title = property.find("h2", class_="title").text.strip()
        price = property.find("p", class_="price").text.strip()
        location = property.find("p", class_="location").text.strip()

        writer.writerow([title, price, location])

print("Data Scraped Successfully!")