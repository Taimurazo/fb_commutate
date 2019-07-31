# todo : registration on facebook from different users
# todo : pin to each user a callback that executes when user recives a message.
# todo : send private message from user.

# users = []
# users.append(User(, 'Iskander1988'))
# users.append(User('taimerlance@gmail.com', ))

from fbchat import Client
from fbchat.models import *


class MyClient(Client):

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
        with open('test.txt', 'w') as out_file:
            out_file.write(10)
        # self.markAsDelivered(thread_id, message_object.uid)
        # self.markAsRead(thread_id)
        #
        #
        # # If you're not the author, echo
        # if author_id != self.uid:
        #     self.send(message_object, thread_id=thread_id, thread_type=thread_type)


if __name__ == '__main__':
    client1 = MyClient('bitakovt@gmail.com', 'Iskander1988')
    client2 = MyClient('taymerlance@gmail.com', 'Iskander1988')

    client1.send(Message(text='test message from bitakov'), thread_id=client1.uid, thread_type=ThreadType.USER)
    client2.send(Message(text='test message from taymerlance'), thread_id=client1.uid, thread_type=ThreadType.USER)

