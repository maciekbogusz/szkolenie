# 
# number = input("Enter number: ")
# print("You entered: "+number)
# float_number = float(number)
# 
# if float_number >= 0.9:
#     print("A")
# elif float_number >= 0.8 :
#     print("B")
# elif float_number >= 0.7 :
#     print("C")
# elif float_number >= 0.6 :
#     print("D")
# else:
#     print("A")    

# Ask user for amount of hours worked in a week and the hourly rate.
# Apply 1.5x modifier for overtime work (over 40 hour per week) and print how much user should get paid.
  
hours = input("Please enter hours: ")
rate = input("Please enter rate: ")
float_hours = float(hours)
float_rate = float(rate)
multiplier = 1.5
hours = 40
if float_hours > hours:
    overtime = float_hours - hours
    pay = (overtime*multiplier*float_rate)+(hours*multiplier)
    print(pay)
elif float_hours <= hours:
    pay = hours*multiplier
    print(pay)
