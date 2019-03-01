import ipaddress
import datetime

huge_list = [ipaddress.ip_network('192.168.{}.0/24'.format(x)) for x in range(1, 254)]


start = datetime.datetime.now()


def get_subnet(ip, hg_list):
    for i in range(10):
        a = [x for x in hg_list if ipaddress.ip_address(ip) in x]


u = [get_subnet('192.168.{}.120'.format(x), huge_list) for x in range(1, 254)]

print('Total time taken is {}'.format(datetime.datetime.now() - start))

print(u)
