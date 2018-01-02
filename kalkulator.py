def calculator(operand1, operand2):
    if operator == "+":
        result = operand1+operand2
    elif operator == "-":
        result = operand1-operand2
    elif operator == "*":
        result = operand1*operand2
    elif operator == "/":
        if float_operand2 > 0: 
            result = operand1/operand2
        else:
            print("Can`t divide by zero")
    return result
            
operators = ["+", "-", "*", "/"]         
condition = "Yes"
result1 = 0

while condition == "Yes":
      operand1 = input("Please enter number: ")
      operator = input("Please enter operator: ")
      operand2 = input("Please enter number: ")    
      if operand1.isnumeric() == True & operand2.isnumeric() == True:
            float_operand1 = float(operand1)
            float_operand2 = float(operand2)
            for elenent in operators:
                  if operator == elenent:
                        result = calculator(float_operand1, float_operand2) 
                        result1 = result +  result1
                        print(result1)
                        condition = input("Shall we continue? ")     
      else:
            print("Wrong parameters provided")
else:
      print(result1)