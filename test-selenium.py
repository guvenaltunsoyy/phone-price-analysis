import numpy as np
#import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


driver_path = "D:/pyhton/chromedriver.exe"
browser = webdriver.Chrome(executable_path=driver_path)
next_url = "https://www.sahibinden.com/iphone-8?date=30days&pagingOffset=40"
a = []
browser.get(next_url)
while next_url != "":
    try:
        options = Options()
        ua = UserAgent()
        userAgent = ua.random
        options.add_argument(f'user-agent={userAgent}')
        driver = webdriver.Chrome(chrome_options=options,
                                  executable_path=driver_path)
        prices = browser.find_elements_by_class_name('searchResultsPriceValue')
        for price in prices:
            b = price.text.split()
            a.append(float(b[0]))
        next_url = browser.find_element_by_partial_link_text(
            'Önceki').get_attribute("href")
        print(next_url)
        page_number = browser.find_element_by_class_name('mbdef').text
        print(page_number)
        next_url = browser.find_elements_by_css_selector(
            'a.prevNextBut').get_attribute('href')
        browser.get(next_url)
    except :
        print(" bitti")
        next_url = ""

browser.close()
print(a)
all_prices = np.array(a)
print(all_prices.mean())
