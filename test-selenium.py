import numpy as np
#import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import traceback
import logging
import re


driver_path = "C:/Users/Phygitalmind/Desktop/twitter-app/phone-price-analysis/chromedriver.exe"
browser = webdriver.Chrome(executable_path=driver_path)
next_url = "https://www.sahibinden.com/iphone-8?date=30days"
a = []
count = 0
browser.get(next_url)
pattern = "[1-9][0-9]*\.[0-9]*"
while next_url != "":
    try:
        count += 1
        options = Options()
        ua = UserAgent()
        userAgent = ua.random
        options.add_argument(f'user-agent={userAgent}')
        driver = webdriver.Chrome(
            chrome_options=options, executable_path=driver_path)
        next_url = browser.find_element_by_partial_link_text(
            'Sonraki').get_attribute("href")
        print(next_url)
        page_number = browser.find_element_by_class_name('mbdef').text
        print(page_number)
        prices = browser.find_elements_by_class_name('searchResultsPriceValue')
        for price in prices:
            b = price.text.split()
            res = re.fullmatch(pattern, b[0])
            if res:
                a.append(float(b[0])*1000)
        browser.get(next_url)
    except ValueError:
        print('ValueError')
        browser.get(next_url)
    except Exception as e:
        logging.error(traceback.format_exc())
        print(" HATA *********")
        browser.close()
        break

print(a)
all_prices = np.array(a)
print(all_prices.mean())
browser.close()
browser.quit()


# price = "99000"
# result = re.match(price, pattern, flags=0)
# res = re.fullmatch(pattern, price)
# if res:
#     print('result')
# else:
#     print('false')


# list = ["guru99 get", "guru99 give", "guru Selenium"]
# for element in list:
#     z = re.match("(g\w+)\W(g\w+)", element)
# if z:
#     print((z.groups()))
