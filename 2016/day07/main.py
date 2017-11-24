#!/usr/bin/env python
from __future__ import print_function
import re
import operator
from functools import reduce


def break_ipv7(ipv7):
    hypernets = re.findall('[[][a-z]+[]]', ipv7)
    ip_parts = re.split('|'.join(map(re.escape, hypernets)), ipv7)
    return hypernets, ip_parts

def is_abba(s):
    return s[0] != s[1] and s[1] == s[2] and s[0] == s[3]

def get_abbas(s):
    return (s[i:i+4] for i in range(len(s) - 3) if is_abba(s[i:i+4]))

def supports_tls(ipv7):
    hypernets, ip_parts = break_ipv7(ipv7)
    
    hypernets_abbas = reduce(operator.add, map(list, map(get_abbas, hypernets)), [])

    if hypernets_abbas:
        return False

    ip_abbas = reduce(operator.add, map(list, map(get_abbas, ip_parts)), [])

    return bool(ip_abbas)


def is_aba(s):
    return s[0] == s[2] and s[0] != s[1]

def get_abas(s):
    return (s[i:i+3] for i in range(len(s)-2) if is_aba(s[i:i+3]))

def supports_ssl(ipv7):
    hypernets, ip_parts = break_ipv7(ipv7)
    
    hypernets_abas = set(reduce(operator.add, map(list, map(get_abas, hypernets)), []))
    ip_abas = set(reduce(operator.add, map(list, map(get_abas, ip_parts)), []))
    
    if not hypernets_abas and not ip_abas:
        return False
    
    else:
        for aba in hypernets_abas:
            if aba[1] + aba[0] + aba[1] in ip_abas:
                return True
    
    return False


assert supports_tls('abba[mnop]qrst') is True
assert supports_tls('abcd[bddb]xyyx') is False
assert supports_tls('aaaa[qwer]tyui') is False
assert supports_tls('ioxxoj[asdfgh]zxcvbn') is True

with open('input.txt') as f:
    ips = f.read().split('\n')

print("Task 1 - solution =", sum(map(supports_tls, ips)))

print("Task 2 - solution =", sum(map(supports_ssl, ips)))
