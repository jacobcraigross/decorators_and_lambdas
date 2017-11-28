
# decorators arent used a TON but sometimes they are super useful.

import functools

def my_dec(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print('inside the decorator!')
        func()
        print('after the decorator!')
    return function_that_runs_func

@my_dec
def my_function():
    print('im the function')

# my_function()

# ---------- more adv. dec stuff below

def decorator_with_arguments(number):
    def my_dec(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print('INNNNN')
            if number == 56: # this feature is used alot in ADMIN permissions
                print('not running!!!!!!')
            else:
                func(*args, **kwargs)
            print('OOOOUUTTTT')
        return function_that_runs_func
    return my_dec

@decorator_with_arguments(66)
def my_function_too():
    print ('hello jacob')

my_function_too()
