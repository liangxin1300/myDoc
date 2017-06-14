#!/usr/bin/env python
#-*-coding: utf-8-*-

import string
import random

KEY_LEN = 20
KEY_NUM = 200

def key_base():
    return string.letters + string.digits

def key_gen_raw():
    key_list = [random.choice(key_base()) for i in range(KEY_LEN)]
    return "".join(key_list)

def key_gen(num=KEY_NUM):
    res = []
    for i in range(num):
        res.append(key_gen_raw())
    return res

if __name__ == "__main__":
    print(key_gen())
