import time

def f():
    print("Hello World")

def job_scheduler(g,n):
    n = n/1000
    time.sleep(n)
    return g()


job_scheduler(f,4000)