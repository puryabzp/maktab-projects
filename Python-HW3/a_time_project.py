from datetime import *
def weekday_generator(a,b,week_day):
        start_date=datetime.strptime(a,'%Y-%m-%d')
        end_date=datetime.strptime(b,'%Y-%m-%d')
        for n in range(int ((end_date - start_date).days)+1):
            if ((start_date + timedelta(n)).weekday())==week_day:
                    a=start_date + timedelta(n)
                    b=a.strftime("%Y %B %d")
                    yield b
result=weekday_generator("2015-12-20","2016-1-11" ,3)
print(result.__next__())
print(result.__next__())







"""print output without .___next___()

from datetime import *
def weekday_generator(a,b,week_day):
        start_date=datetime.strptime(a,'%Y-%m-%d')
        end_date=datetime.strptime(b,'%Y-%m-%d')
        for n in range(int ((end_date - start_date).days)+1):
            if ((start_date + timedelta(n)).weekday())==week_day:
                    a=start_date + timedelta(n)
                    b=a.strftime("%Y %B %d")
                    yield b
result=weekday_generator("2015-12-20","2016-1-11" ,2)
for i in result:
        print(i)