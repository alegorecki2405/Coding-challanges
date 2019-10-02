import time

def f():
    print("Hello World")

def job_scheduler(g,n):
    time.sleep(n)
    return g()


job_scheduler(f,4)