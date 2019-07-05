import multiprocessing
import threading
import time
from telnetlib import Telnet


def telnet_connect(ipaddr):
    print("telnet connecting", ipaddr)
    try:
        telnet = Telnet(ipaddr, 23, timeout=5)
    except:
        pass


if __name__ == '__main__':
    start_time = time.time()

    jobs = []

    equip_list = ["1.1.1.1", "1.1.1.2", "1.1.1.3"]
    # equip_list = ["1.1.1.1"]

    for ipaddr in equip_list:
        # thread = threading.Thread(target=telnet_connect, args=(ipaddr, ))
        thread = multiprocessing.Process(target=telnet_connect, args=(ipaddr,))
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("--- 걸린시간 : %s seconds ---" % (time.time() - start_time))

