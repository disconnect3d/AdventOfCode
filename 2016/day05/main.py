#!/usr/bin/env python
from __future__ import print_function
from hashlib import md5


def get_pass(input_):
    passwd = ''
    idx = 0
    
    while len(passwd) < 8:
        hashed = md5(input_ + str(idx)).hexdigest()
        
        if hashed.startswith('00000'):
            passwd += hashed[5]
        idx += 1
    
    return passwd


def get_pass_with_position(input_):
    passwd = [b'.'] * 8
    idx = 0
    
    while '.' in passwd:
        hashed = md5(input_ + str(idx)).hexdigest()
        
        if hashed.startswith('00000'):
            if hashed[5] in '01234567':
                pos = int(hashed[5])
                if passwd[pos] == '.':
                    passwd[pos] = hashed[6]

        idx += 1
    
    return ''.join(passwd)


assert get_pass('abc') == '18f47a30'
print("Task1 solution =", get_pass('ojvtpuvg'))
print("Task2 solution =", get_pass_with_position('ojvtpuvg'))
