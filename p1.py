week_hours = float(input("Enter weekly working hours : "))
hourly_pay = float(input("Enter pay rate per hour : "))
working_weeks = float(input("Enter working weeks in a month : ")) 
monthly_pay = week_hours * hourly_pay * working_weeks
print("Calculated monthly pay : Rs", monthly_pay)