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

# Scrape for the hogwarts staff
driver.get('https://harrypotter.fandom.com/wiki/Hogwarts_Legacy')
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
for atts in physical_atts:
    for staff in hogwarts_staff:
        driver.get(staff['url'])
        titles = driver.find_elements(By.XPATH, f'//*[@id="mw-content-text"]/div/aside/section[3]/div/h3')
        values = driver.find_elements(By.XPATH, f'//*[@id="mw-content-text"]/div/aside/section[3]/div[{physical_atts.index(atts)+1}]/div')
        for title in titles:
                if title.text.lower() == atts:
                    for value in values:
                        staff[atts]=value.text

# Scrape for the hogwarts students by house
