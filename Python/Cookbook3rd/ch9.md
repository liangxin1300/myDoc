## Metaprogramming
#### Putting a Wrapper Around a Function
```python
# A decorator is a function that accepts a function as input
# and returns a new function as output
# built-in decorator such as @staticmethod @classmethod and
# @property work in the same way
import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1

countdown(10000)
func = timethis(countdown)
func(10)
```
#### Preserving Function Metadata When Writing Decorators
```python
# You're written a decorator, but when you apply it to a function,
# import metadata such as the name, doc string, annotations, and
# calling signature are lost
import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n:int):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

countdown(100000)
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)
```
```python
# Copying decorator metadata is an import part of writing decorators.
# If you forget to use @wraps, you'll find that the decorated function
# loses all sorts of usefull information
import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time
    '''
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n:int):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

countdown(100000)
print(countdown.__name__) # wrapper
print(countdown.__doc__)  # None
print(countdown.__annotations__) # {}
```
#### Unwrapping a Decorator
```python
# A decorator has been applied to a function, but you want to "undo" it,
# gainning access to the original unwapped function
import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def add(x, y):
    return x + y

add(3, 4)
orig_add = add.__wrapped__
print(orig_add(3, 4))
# Gaining direct access to the unwrapped function behind a decorator can be
# useful for debugging, introspection, and other operations involving functions.
# However, this recipe works if the implementation of a decorator properly
# copies metadata using @wraps from the functools module or sets the
# __wrapped__ attribute directly
```
#### Defining a Decorator That Takes Arguments
