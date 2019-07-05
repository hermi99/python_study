import multiprocessing
import threading
import time
from telnetlib import Telnet

def telnet_connect(main, ipaddr):
    print("telnet connecting", ipaddr)
    print("main:", main)
    try:
        telnet = Telnet(ipaddr, 23, timeout=5)
    except:
        pass


class Main:
    def execute(self):
        jobs = []

        equip_list = ["1.1.1.1", "1.1.1.2", "1.1.1.3"]
        # equip_list = ["1.1.1.1"]

        for ipaddr in equip_list:
            thread = threading.Thread(target=telnet_connect, args=(self, ipaddr, ))
            # thread = multiprocessing.Process(target=telnet_connect, args=(self, ipaddr,))
            jobs.append(thread)

        for j in jobs:
            j.start()
            # j.run()

        for j in jobs:
            j.join()



if __name__ == '__main__':
    # start_time = time.time()
    #
    # jobs = []
    #
    # equip_list = ["1.1.1.1", "1.1.1.2", "1.1.1.3"]
    # # equip_list = ["1.1.1.1"]
    #
    #
    # for ipaddr in equip_list:
    #     # thread = threading.Thread(target=telnet_connect, args=(ipaddr, ))
    #     thread = multiprocessing.Process(target=telnet_connect, args=(ipaddr,))
    #     jobs.append(thread)
    #
    # for j in jobs:
    #     j.start()
    #
    # for j in jobs:
    #     j.join()
    #
    # print("--- 걸린시간 : %s seconds ---" % (time.time() - start_time))

    main = Main()
    main.execute()
