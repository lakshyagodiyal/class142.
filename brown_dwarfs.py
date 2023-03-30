from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("C:\Users\mohak\OneDrive\Desktop")
browser.get(START_URL)

time.sleep(10)

new_planets_data = []

def scrape_more_data(hyperlink):
    print(hyperlink)
    
    ## ADD CODE HERE ##
    try:
        page=requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        temp_list=[]
        for tr_tag in soup.find_all("tr", attrs={"distance", "fact_row"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                    
                    try:
                        temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                    except:

                        temp_list.append("")
        new_planets_data.append(temp_list)

    except:
     time.sleep(1)
     scrape_more_data(hyperlink)

brown_dwarfs = pd.read_csv("updated_scraped_data.csv")





# Remove '\n' character from the scraped data
scraped_data = []

for row in new_planets_data:
    replaced = []
    ## ADD CODE HERE ##
    for i in row:
        i = i.replace("\n", "")
        replaced.append(i)


    
    scraped_data.append(replaced)

print(scraped_data)

headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity", "detection_method"]

new_planet_df_1 = pd.DataFrame(scraped_data,columns = headers)

# Convert to CSV
new_planet_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")
