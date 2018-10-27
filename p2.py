eid=input("Enter employee id :")
basic=float(input("Enter basic salary : "))
allowances=float(input("Enter allowances : "))
gross=basic+allowances
if(gross<=5000):
    tax=0
elif(gross<=10000):
    tax=0.1*gross
elif(gross<=20000):
    tax=0.2*gross
else:
    tax=0.3*gross
netpay=gross-tax
print("Employee id : ",eid)
print("Basic salary : ",basic)
print("Allowances : ",allowances)
print("Gross pay : ",gross)
print("Tax : ",tax)
print("Netpay : ",netpay)
