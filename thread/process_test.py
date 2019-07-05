
import random
import multiprocessing
import time


def list_append(count, id, out_list):
	"""
	Creates an empty list and then appends a
	random number to the list 'count' number
	of times. A CPU-heavy operation!
	"""
	for i in range(count):
		out_list.append(random.random())

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000   # Number of random numbers to add
    procs = 2   # Number of processes to create

    jobs = []
    for i in range(0, procs):
    	out_list = list()
    	process = multiprocessing.Process(target=list_append,
			                              args=(size, i, out_list))
    	jobs.append(process)

    for j in jobs:
    	j.start()

    for j in jobs:
    	j.join()

    print("--- 걸린시간 : %s seconds ---" % (time.time() - start_time))
