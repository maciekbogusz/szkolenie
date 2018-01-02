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
temp_condition = condition = "YES"
temp_result = 0

while temp_condition.upper() == condition:
      operand1 = input("Please enter number: ")
      operator = input("Please enter operator: ")
      operand2 = input("Please enter number: ")    
      if operand1.isnumeric() == True & operand2.isnumeric() == True:
            float_operand1 = float(operand1)
            float_operand2 = float(operand2)
            for elenent in operators:
                  if operator == elenent:
                        result = calculator(float_operand1, float_operand2) 
                        temp_result = result +  temp_result
                        print(temp_result)
                        temp_condition = input("Shall we continue? ")     
      else:
            print("Wrong parameters provided")
else:
      print(temp_result)