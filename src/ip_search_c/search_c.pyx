

import cython
# import ipaddress
from  libc.ipaddress cimport ip_network

def get_subnet():
    # with nogil:
    a = 20
    # a = ip_network('192.168.1.0/24')


# def get_subnet2(cython.str ip, cython.str ip2):
#     huge_list = [ip_network('192.168.{}.0/24'.format(x)) for x in range(1, 254)]
#     a = [get_subnet('192.168.{}.120'.format(x), huge_list) for x in range(1, 254)]
#     return a