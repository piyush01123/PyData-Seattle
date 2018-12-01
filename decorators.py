from time import time

def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('%s ran in %s microseconds' %(func.__name__, after-before))
        return rv
    return f

def ntimes(n=1):
    def inner(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print('Running %s for the %sth time' %(func.__name__, _))
                rv = func(*args, **kwargs)
            return rv
        return wrapper
    return inner

@timer
@ntimes(2)
def add(x, y=10):
    return x+y

@timer
@ntimes(3)
def sub(x, y=10):
    return x-y

print(add(20))
print(add(20, 30))
print(sub(20))
print(sub(20, 30))
