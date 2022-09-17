from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("https://exoplanets.nasa.gov/exoplanet-catalog/")
browser.get(START_URL)
time.sleep(10)
def scrape() :
    headers = ["Name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
    for i in range(1, 5):
        while True:
            time.sleep(2)
            soup = BeautifulSoup(browser.page_source, "html.parser")
            current_page_num = int(soup.find_all("input", attrs = {"class", "page number"})[0].get("value"))
            if current_page_num < i:
                browser.find_element(By.XPATH, value = '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif current_page_num > i:
                browser.find_element(by.XPATH, value = '//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else :
                break
        for ul_tag in soup.find_all("ul", attrs = {"class", "exponent"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tags in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tags.find_all("a")[0]).contents[0]
                else :
                    try : 
                        temp_list.append(li_tags.contents[0])
                    except : 
                        temp_list.append("")