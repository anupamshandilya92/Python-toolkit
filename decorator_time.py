# -*- coding: utf-8 -*-
"""
Created on 12/29/2019

@author: Anupam Shandilya
"""



#Decorator for timing
def my_timer(orig_func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in {} seconds.'.format(orig_func.__name__,t2))
        return result
    return wrapper


##Usage
@my_timer
def display():
    print('Anupam')
