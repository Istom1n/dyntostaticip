"""
Change A record for you domain if your IP address was dynamic.
Tested on Xiaomi Mini and NS1.com DNS platform

Written by: Ivan Istomin
Date: 31.01.2019
Version: 0.0.1

So said to do Guido:
PEP 484 (https://www.python.org/dev/peps/pep-0484/)
PEP 526 (https://www.python.org/dev/peps/pep-0526/)
"""

import pymiwifi
from ns1 import NS1, records

import sys

MIWIFI_PASS = sys.argv[1]
NS1_API = sys.argv[2]
DOMAIN_FOR_UPDATE = sys.argv[3]


def define_new_ip() -> str:
    miwifi = pymiwifi.MiWiFi()
    miwifi.login(MIWIFI_PASS)

    return miwifi.pppoe_status()['ip']['address']


def update_record_a(ip: str) -> bool:
    ns1_api: NS1 = NS1(apiKey=NS1_API)
    record: records = ns1_api.loadRecord(DOMAIN_FOR_UPDATE, 'A')
    upd_ip = record.data['answers'][0]['answer'][0]

    if isinstance(upd_ip, str) and ip is not upd_ip:
        record.update(answers=[ip])

        return True

    return False


if __name__ == "__main__":
    print('Getting new IP address:')
    ip: str = define_new_ip()
    print(ip)

    print('Updating A record on DNS server')
    if update_record_a(ip): print('A record updated successfully!')
    else: print('An error has occurred!')
