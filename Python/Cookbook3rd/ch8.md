## Classes and Objects

#### Changing the String Representation of Instances
```python
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)
```

#### Customizing String Formatting
```python
_formats = {
    'ymd': '{d.year}--{d.month}--{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2013, 12, 21)
print(format(d))
print(format(d, 'mdy'))
```

#### Making Objects Support the Context-Management Protocol
```python
from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None

from functools import partial

conn = LazyConnection(('www.python.org', 80))
with conn as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))

print(resp)
```

#### Saving Memory When Creating a Large Number of Instances
```python
class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
```

#### Creating Managed Attributes
```python
# You want to add extra processing(e.g., type checking or validation) to
# the getting or setting of an instance attribute
class Person:
    def __init__(self, first_name):
        self.first_name = first_name #call the setter
 
    # getter function
    @property
    def first_name(self):
        return self._first_name

    # setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Execpted a string')
        self._first_name = value

    # deleter function
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

a = Person('liang')
print(a.first_name) # calls the getter

a.first_name = "xin" # calls the setter
print(a.first_name) # calls the getter
```

#### Calling a Method on a Parent Class
```python
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

b = B()
b.spam()
```
```python
class A:
    def __init__(self):
        self.x = 0
class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1
```
