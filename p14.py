def leapyear(y):
    if(y%4!=0):
        return False
    if(y%100==0):
        if(y%400==0):
            return True
        else:
            return False
    else:
        return True
def numberOfDaysInAYear(year):
    if(leapyear(year)):
        return 366
    else:
        return 365

for i in range(2010,2021):
    print("No of days in ",i," is ",numberOfDaysInAYear(i))