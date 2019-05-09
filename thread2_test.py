import multiprocessing
import random
import threading
import time


def list_append(count, id, out_list):
	for i in range(count):
		out_list.append(random.random())

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000   # Number of random numbers to add
    threads = 4   # Number of threads to create

    # for i in range(0, threads):
    #     list_append(size, i, list())

    jobs = []
    for i in range(0, threads):
        out_list = list()
        # thread = threading.Thread(target=list_append, args=(size, i, out_list))
        thread = multiprocessing.Process(target=list_append, args=(size, i, out_list))
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()



    print("--- 걸린시간 : %s seconds ---" % (time.time() - start_time))

