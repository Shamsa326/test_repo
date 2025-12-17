
#import library 

import datetime

#define a function to return date and day in certain format

def get_today_date ():
    
    ts_date= datetime.datetime.now()
    v=ts_date.strftime("%S:%M:%H,%d/%m,%Y")
    return v 

#call the fuction to print 
print(get_today_date())
    

#define a function to use current time tp display Fibonacci Seq

def current_time ():
     ts_date= datetime.datetime.now()
     S= ts_date.minute
     n= S*2 # as required in question to find 2 * current min 
     #create fibonacci sequences 
     K=[]
     a,b=0,1
     for i in range(n):
      K.append(a) #add the number 
      a,b = b, a+b
     return K

print(current_time ())
