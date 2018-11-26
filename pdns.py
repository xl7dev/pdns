#!/usr/bin/env python
# encoding: utf-8

"""
@author: xl7dev
"""
from mysqlDB import MysqlDB
from scapy.all import sniff, dnsqtypes, UDP, DNSQR, conf

# disable verbose mode
conf.verb = 0
demo = MysqlDB(host='127.0.0.1', user='root', pwd='toor', port=3306, db="pdns")


def dns_sniff(pkt):
    if pkt.haslayer(DNSQR) and UDP in pkt and pkt[UDP].sport == 53:
        udp = pkt['UDP']
        dns = pkt['DNS']
        if int(udp.sport) == 53:
            try:
                for i in range(dns.ancount):
                    dnsrr = dns.an[i]
                    name = dnsrr.rrname.decode().strip('.')
                    type = dnsqtypes[dnsrr.type]
                    value = dnsrr.rdata
                    if isinstance(value, bytes):
                        value = dnsrr.rdata.decode().strip('.')
                    print("[*] {0} {1} {2}".format(name, type, value))
                    demo.insert(name, type, value)
            except Exception as e:
                print(pkt, e)


if __name__ == "__main__":
    sniff(iface="en0", filter='udp and port 53', store=0, prn=dns_sniff)
