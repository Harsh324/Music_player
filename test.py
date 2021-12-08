from threading import Thread
import _thread
from time import sleep

def hello():
    for i in range(5):
        print("Hello")
        sleep(0.2)

def hi():
    for i in range(5):
        print("Hi")
        sleep(0.2)

t1 = Thread(target=hello)
t2 = Thread(target=hi)

t1.start()
t2.start()
print("**")
