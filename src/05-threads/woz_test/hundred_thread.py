
import threading
import time
import math

start = time.time()


def do_math(start=0, num=100):
    pos = start
    k_sq = 1000 * 1000
    while pos < num:
        pos += 1
        math.sqrt((pos - k_sq) * (pos - k_sq))


def time_waste():
    a = 10000*10000*1200000*55555555*99999*77777*55555
    b = 10000 * 10000 * 1200000 * 55555555 * 99999 * 77777 * 55555
    n = 10000 * 10000 * 1200000 * 55555555 * 99999 * 77777 * 55555
    v = 10000 * 10000 * 1200000 * 55555555 * 99999 * 77777 * 55555
    u = 10000 * 10000 * 1200000 * 55555555 * 99999 * 77777 * 55555
    g = 10000 * 10000 * 1200000 * 55555555 * 99999 * 77777 * 55555
    f = 10000 * 10000 * 1200000 * 55555555 * 99999 * 77777 * 55555
    do_math(99999, 9999999)
    time.sleep(1)


threads = [threading.Thread(target=time_waste) for x in range(4000)]
[th.start() for th in threads]
print('{} of threads now going to close them...'.format(len(threads)))
[th.join() for th in threads]


print('Total time is {} Seconds'.format(time.time() - start))