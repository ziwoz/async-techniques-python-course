import aio_ping

from aio_ping import ping

# a = ping('google.com', timeout=3000, count=3, delay=0.5)


def main():
    for i in range(100):
        a = ping('google.com', count=1)
        print('The value of a in this is {}'.format(a))

if __name__ == 'main':
    main()

main()