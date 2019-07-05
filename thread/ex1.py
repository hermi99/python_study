import threading
import time


class PrintTime(threading.Thread):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            time.sleep(self.interval)
            print(time.ctime(time.time()))

if __name__ == '__main__':
    t = PrintTime(5)
    t.start()

    while(True): pass