def calculator(operand1, operand2):
    if operator == "+":
        result = operand1+operand2
        print(result)
    elif operator == "-":
        result = operand1+operand2
        print(result)
    elif operator == "*":
        result = operand1*operand2
        print(result)
    elif operator == "/":
        if float_operand2 > 0: 
            result = operand1/operand2
            print(result)
        else:
            print("Can`t divide by zero")

# def check_operands(number1):
#     if type(number1) == int or type(number1) == float:
#         number = float(number1)
#         return number
#             
operand1 = input("Please enter number: ")
operator = input("Please enter operator: ")
operand2 = input("Please enter number: ")

float_operand1 = float(operand1)
float_operand2 = float(operand2)

calculator(float_operand1, float_operand2)

cont = input("Shall we continue? ")
if cont == "Yes":
    calculator(operand1, operand2)
elif cont == "No":
    print("Thank you ")
