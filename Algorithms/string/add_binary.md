```Python
"""
Given two binary strings,
return their sum (also a binary string)

For example,
a = "11"
b = "1"
return "100"
"""

def add_binary_1(a, b):
    s = ""
    c, i, j = 0, len(a)-1, len(b)-1
    zero = ord('0')
    while(i >= 0 or j >= 0 or c == 1):
        if i >= 0:
            c += ord(a[i]) - zero
            i -= 1
        if j >= 0:
            c += ord(b[j]) - zero
            j -= 1
        s = chr(c % 2 + zero) + s
        c //= 2
    return s

def add_binary_2(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

print(add_binary_1("11", "1"))
print(add_binary_2("11", "1"))
```
