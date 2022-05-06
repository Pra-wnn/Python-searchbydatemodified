import os 
import time
import datetime as dt

i=0

while i==0:
    kw = input("Enter Path :")
    dw = input('Enter a date in DD/MM/YYYY format: ')
    if dw != "" and os.path.exists(kw):
        year, month, day = map(int, dw.split('/'))
        d1 = dt.datetime(day,month,year)
        d11 = d1.date()
        for dirpath, dirnames,file in os.walk(kw):
                for filename in file:
                    f = '/'.join([dirpath,filename]) 
                    df1 = (os.path.getctime(f)) 
                    df1 = time.strftime(  '%m/%d/%Y',
                                time.gmtime(os.path.getctime(f))) 
                    d2 = dt.datetime.strptime(df1,'%m/%d/%Y').date()
                    if d11 == d2:
                        print(f)
    else:
        i = i+1



