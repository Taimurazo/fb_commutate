import time, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-private')
browsers_number = 5

browsers = []
for i in range(browsers_number):
    browsers.append(webdriver.Firefox(options=options))
    # browsers[i].get('http://www.ubuntu.com/')

