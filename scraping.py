from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import pandas as pd

# Start chrome in background without any visual output or windows
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1200")

# Initialize the driver
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
driver.get('https://harrypotter.fandom.com/wiki/Hogwarts_Legacy')

def physical_attributes(nested_list):
    '''
    This function takes in a list of dictionaries, loops through it and
    appends the physical attributes scraped from the characters to it
    '''
    physical_atts = ['species', 'gender', 'hair colour', 'eye colour','skin colour']
    for atts in physical_atts:
        for value in nested_list:
            try: 
                driver.get(value['url'])
                titles = driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div/aside/section[3]/div/h3')
                attributes = driver.find_elements(By.XPATH, f'//*[@id="mw-content-text"]/div/aside/section[3]/div[{physical_atts.index(atts)+1}]/div')
                for title in titles:
                    if title.text.lower() == atts:
                        for attribute in attributes:
                            value[atts] = attribute.text
            except:
                pass
    return nested_list
# Scrape for the hogwarts staff
elements = driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div/ul[6]/li/a[1]')
hogwarts_staff = []
physical_atts = ['species', 'gender', 'hair colour', 'eye colour','skin colour']
for element in elements:
    hogwarts_staff.append({
        'staff': element.text,
        'url':element.get_attribute('href'),
        'species': None,
        'gender': None,
        'hair colour': None,
        'eye colour': None,
        'skin colour': None
        })
physical_attributes(hogwarts_staff)

# Scrape for the hogwarts students by house
house_names = ['Hufflepuff', 'Gryffindor', 'Ravenclaw', 'Slytherin']
houses_students = []
for name in house_names:
    if name == 'Gryffindor':
        xpaths = [f'//*[@id="mw-content-text"]/div/ul[{house_names.index(name)+2}]/li/a',f'//*[@id="mw-content-text"]/div/ul[{house_names.index(name)+2}]/li[10]/span']
    else:
        xpaths = [f'//*[@id="mw-content-text"]/div/ul[{house_names.index(name)+2}]/li/a',f'//*[@id="mw-content-text"]/div/ul[{house_names.index(name)+2}]/li[10]/span']
    for xpath in xpaths:
        houses = driver.find_elements(By.XPATH, xpath)
        for house in houses:
            houses_students.append({
                'house': name,
                'student': house.text,
                'url': house.get_attribute('href'),
                'species': None,
                'gender': None,
                'hair colour': None,
                'eye colour': None,
                'skin colour': None
            })
physical_attributes(houses_students)
# Scraping for the historical wizards
