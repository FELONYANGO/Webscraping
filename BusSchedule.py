#BusSchedule.py
#Name:
#Date:
#Assignment:

import datetime
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import bs4  
import requests
import buss


#driver = webdriver.Chrome("chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def loadURL(url):
    """
    This function loads a given URL and returns the text
    that is displayed on the site. It does not return the
    raw HTML code but only the code that is visible on the page.
    """
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--headless");
    #driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get(url)
    page = driver.page_source
    # content=driver.find_element(By.XPATH, "/html/body").text
    driver.quit()
    soup = bs4.BeautifulSoup('html5lib') 

    return soup.schedule

def loadTestPage():
    """
    This function returns the contents of our test page.
    This is done to avoid unnecessary calls to the site
    for our testing.
    """
    page = open("text page.txt", 'r')
    contents = page.read()
    page.close()

    return contents


def parsePage(contents):
    soup = BeautifulSoup(contents, "html.parser")

    print(soup.all)

    # for list in soup.find_all('ul'):
    #     print(list.get('ul'))


def main():
    url = "https://myride.ometro.com/Schedule?stopCode=3060&routeNumber=5&directionName=EAST"
    c1 = loadURL(url) #loads the web page
    # c1 = loadTestPage() #loads the test page
    # current_time = datetime.utcnow()
 
# Printing value of now.
    # print("Time now at greenwich meridian is:", current_time)
    # print(c1)
    # parsePage(c1)

main()
buss()
