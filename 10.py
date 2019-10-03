# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.


import time

def f():
    print("Hello World")

def job_scheduler(g,n):
    n = n/1000
    time.sleep(n)
    return g()


job_scheduler(f,4000)