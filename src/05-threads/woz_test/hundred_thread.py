
import threading
import time

start = time.time()


def time_waste():
    a = 10000*10000*1200000*55555555
    time.sleep(1)


threads = [threading.Thread(target=time_waste) for x in range(4000)]
[th.start() for th in threads]
print('{} of threads now going to close them...'.format(len(threads)))
[th.join() for th in threads]


print('Total time is {} Seconds'.format(time.time() - start))