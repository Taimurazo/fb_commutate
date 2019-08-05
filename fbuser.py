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
        """

        Args:
            callback:  custom callback.
        Returns: None

        """
        if callback != None:
            self._callback = callback
        else:
            raise ValueError("callback can't be None.")

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
        """
        Executes callback when message recived.
        Args:
            mid:
            author_id: - id of message author
            message: - message text (deprecated. use message_object.text)
            message_object:
            thread_id:
            thread_type:
            ts: message timestamp
            metadata:
            msg:

        Returns:

        """
        if author_id != self.uid:
            self._callback(message_object.text, author_id, ts, self)
        else:
            print("Self messaging not alowed to avoid infinite looping. user id = %s" % author_id)


class FBAssenbler:

    def __init__(self):
        self.users = {}
        self._threads = []

    def add_user(self, email, pswd, callback):
        """
        Add user to assemble.
        Args:
            email: user login
            pswd: user password
            callback:  custom callback
        Returns:

        """
        self.users[email] = {'email': email, 'password': pswd, 'callback': callback}

    def _run(self, email):
        """
        Thread function.
        Args:
            email: user login.
        Returns:

        """
        fb_user = FBUser(login=email, password=self.users[email]['password'])
        print("User ID: %s" % fb_user.uid)
        fb_user.set_callback(self.users[email]['callback'])
        fb_user.listen()

    def listen_all_users(self):
        """
        Run all user listeners in separate threads.
        Returns:

        """
        for email in self.users.keys():
            self._threads = threading.Thread(target=self._run, args=(email,))
            self._threads.start()


def callback1(msg_text, from_user_id, timestamp, fb_user):
    """

    Args:
        msg_text: message text.
        user_id: id og message author
        timestamp: message timestamp.
        fb_obj: user object. Can send messages  (send(Message(text='test message '), thread_id=uid, thread_type=ThreadType.USER))

    Returns:

    """
    user_id = 1 # SET VALID USER ID
    fb_user.send(Message(text='ECHO: %s' % msg_text), thread_id=user_id, thread_type=ThreadType.USER)




def one_user():
    asmb = FBAssenbler()
    asmb.add_user("test@gmail.com", 'test', callback1)
    asmb.listen_all_users()


if __name__ == '__main__':
    one_user()
