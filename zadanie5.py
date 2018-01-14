#Rewrite exercise 1, but now instead of printing entire list, print minimal value, maximum value 
#and average of elements in that list (without using built-in min/max/sum functions).
lst = []
stop = 'continue'
while stop != 'done':
    number = input("Enter number: ")
    x = int(number)
    lst.append(x)
    stop = input("Is it done? ")
print(lst)

#sum / average
result = 0
for element in lst:
    len_of = len(lst)
    result = result + element
    average = result/len_of
print("Sum of elements:",result)
print("Average is:",average) 

#min / max
result = 0
i = 0
min_list = lst[0]
for element in lst:
    if element < min_list:
        min_list = element
print("Minimum value:",min_list)
#max
result = 0
i = 0
max_list = lst[0]
for element in lst:
    if element > max_list:
        max_list = element
print("Max value:",max_list)

