from timeit import default_timer as timer
from functools import wraps
import time


'''
from functools import wraps
using decorator @wraps(func) let to save metadata from function

'''


def func_time(func):
    @wraps(func)
    def innerwrapper(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        print(f'Function {func.__name__} took {end - start} for execution')
    return innerwrapper


@func_time
def hi(*args):
    time.sleep(2)
    print(sum(args))
    print('I hate Hello World')


hi(5, 6, 7)


@func_time
def hello():
    time.sleep(3)
    print("hello world")
