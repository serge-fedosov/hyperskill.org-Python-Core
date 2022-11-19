import time
from threading import Thread


def hello_doe():
    time.sleep(3)
    print('Wait a moment...\nHave a great day!')


def hello_doe_first():
    time.sleep(1)
    print('Hello, John Doe!')


t1 = Thread(target=hello_doe)
t2 = Thread(target=hello_doe_first)

t1.start()
t2.start()
