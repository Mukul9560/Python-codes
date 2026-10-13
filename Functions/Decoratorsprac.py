import time
def total_time(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        func(*args,**kwargs)
        end = time.time()
        print("total time",end-start)
    return wrapper

@total_time
def natural_num(n):
    for i in range(1,n+1):
         print(i)
    
@total_time
def pali_num(n):
    for i in range(1,n+1):
        if str(i)[::-1]==str(i):
         print(i)

# natural_num(500)
pali_num(500)