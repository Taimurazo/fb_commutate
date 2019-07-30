from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

from time import sleep


class FBUser:

    def __init__(self):
        self._callback = None
        self._login = ""
        self._password = ""

        self._options = Options()
        self._options.add_argument('-private')

        self._browser = webdriver.Firefox(options=self._options)

    def set_login_password(self, login, password):
        if type(login) == str and type(password) == str:
            self._login = login
            self._password = password
        else:
            raise TypeError("Login and password must be string.")

    def set_callback(self, callback):
        if callback != None:
            self._callback = callback
        else:
            raise ValueError("callback can't be None.")

    def login(self):
        self._browser.get("http://www.facebook.org")
        assert "Facebook" in self._browser.title
        elem = self._browser.find_element_by_id("email")
        elem.send_keys(self._login)
        elem = self._browser.find_element_by_id("pass")
        elem.send_keys(self._password)
        elem.send_keys(Keys.RETURN)
        sleep(5)  # todo replace by waiting function.

    def _switch_to_user_chat(self, first_name, last_name):
        user_class_name = '_1ht6'

        first_name = first_name.split()[0]  # rmove spaces
        last_name = last_name.split()[0]  # rmove spaces
        name = first_name + ' ' + last_name

        users = self._browser.find_elements_by_xpath("//*[contains(text(), '%s')]" % name)
        if len(users) > 0:
            target_user = [user for user in users if user.get_attribute('class') == user_class_name][0]
            target_user_href = target_user.find_element_by_xpath('..') \
                .find_element_by_xpath('..') \
                .find_element_by_xpath('..') \
                .find_element_by_xpath('..')
            target_user_href.click()
        else:
            print("INFO SEND MESSAGE: Target user not found!")

    def _switch_to_textarea(self):
        text_area = self._browser.find_elements_by_xpath("//textarea[@class='uiTextareaAutogrow _552m']")
        print(text_area)

    # todo 1.find user
    # todo 2.find text area
    # todo 3. type texr
    # todo 4. click on send button.
    def send_message(self, first_name, last_name, message_text=''):
        self._browser.get("http://www.facebook.org/messages")
        assert "Messenger" in self._browser.title
        self._switch_to_user_chat(first_name, last_name)
        self._switch_to_textarea()

def one_user():
    f1 = FBUser()
    f1.set_login_password('bitakovt@gmail.com', 'Iskander1988')

    f1.login()
    f1.send_message(first_name='Petr', last_name='Vtoroy', message_text="Hellow")


def two_usere():
    f1 = FBUser()
    f1.set_login_password('bitakovt@gmail.com', 'Iskander1988')

    f1.login()
    f1.send_message(first_name=' ', last_name=' ', message_text="Hellow")

    f2 = FBUser()
    f2.set_login_password('taimerlance@gmail.com', 'Iskander1988')

    f2.login()
    f2.send_message(first_name=' ', last_name=' ', message_text="Hellow")


if __name__ == '__main__':
    one_user()
    # two_usere()
