# import src.ip_search_c.search_c as C_Search
import src.ip_search_c.search_c as S
import datetime
import ipaddress


def search():
    huge_list = [ipaddress.ip_network('192.168.{}.0/24'.format(x)) for x in range(1, 254)]
    start = datetime.datetime.now()
    for i in range(5):
        u = [S.get_subnet('192.168.{}.120'.format(x), huge_list) for x in range(1, 254)]
    print('Time taken is {}'.format(datetime.datetime.now() - start))


def cython_test():
    start = datetime.datetime.now()
    output = S.get_subnet2('a', '192.168.1.0/24')
    print('it took {} seconds'.format(datetime.datetime.now() - start))
    print(output)



def main():
    print(f'testing if its pyton3')
    cython_test()


if __name__ == '__main__':
    main()

