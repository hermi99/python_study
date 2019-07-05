import threading
from time import *

loops = [4, 2, 3, 7, 2, 5, 4, 2, 3, 7, 2, 5]

class MyLoop:

    def loop(self, nloop, nsec):


    def main(self):
        print("starting threads...")
        threads = []

        for i in range(len(loops)):
            t = threading.Thread(target=self.loop,print("start loop", nloop, 'at', ctime(time()))
        # sleep(nsec)
        print("loop", nloop, 'done at', ctime(time()))

                                 args=(i, loops[i]))
            threads.append(t)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print("all Done at:", ctime(time()))



if __name__ == '__main__':
    loop = MyLoop()
    loop.main()