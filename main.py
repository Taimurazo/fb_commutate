# todo : registration on facebook from different users
# todo : pin to each user a callback that executes when user recives a message.
# todo : send private message from user.
#
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys



class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password


users = []
users.append(User('bitakovt@gmail.com', 'Iskander1988'))
users.append(User('taimerlance@gmail.com', 'Iskander1988'))

browsers = []
for user in users:
    browser = webdriver.Firefox(options=options)
browsers.append(browser)
