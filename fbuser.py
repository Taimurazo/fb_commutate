import time

import threading
from fbchat import Client
from fbchat.models import *


class FBUser(Client):

    def __init__(self, login='', password=''):
        self._callback = None
        self._login = login
        self._password = password
        super(FBUser, self).__init__(email=login, password=password)

    def set_callback(self, callback):
        if callback != None:
            self._callback = callback
        else:
            raise ValueError("callback can't be None.")

    def send_message(self, first_name, last_name, message_text=''):
        pass

    def onMessage(
            self,
            mid=None,
            author_id=None,
            message=None,
            message_object=None,
            thread_id=None,
            thread_type=ThreadType.USER,
            ts=None,
            metadata=None,
            msg=None,
    ):
        self._callback(message_object.text, author_id, ts)


class FBAssenbler:

    def __init__(self):
        self.users = {}
        self._threads = []

    def add_user(self, email, pswd, callback):
        self.users[email] = {'email': email, 'password': pswd, 'callback': callback}

    def _run(self, email):
        fb_user = FBUser(login=email, password=self.users[email]['password'])
        fb_user.set_callback(self.users[email]['callback'])
        fb_user.listen()

    def listen_all_users(self):
        for email in self.users.keys():
            self._threads = threading.Thread(target=self._run, args=(email,))
            self._threads.start()



def callback(msg_text, user_id, timestamp):
    print(timestamp, " ", user_id, " ", msg_text)
    print(threading.current_thread().ident)

def one_user():
    # f1 = FBUser('bitakovt@gmail.com', 'Iskander1988')
    # f1.set_callback(callback)
    # f1.listen()
    asmb = FBAssenbler()
    asmb.add_user('taymerlance@gmail.com', 'Iskander1988', callback)
    asmb.add_user('bitakovt@gmail.com', 'Iskander1988', callback)
    asmb.listen_all_users()


if __name__ == '__main__':
    one_user()
