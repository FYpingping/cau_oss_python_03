def sum(x, y):
     return (x+y)
def sub(x, y):
     return (x - y)
def arithmetic_ops(op):
     num1 = int(input("Input number1: "))
     num2 = int(input("Input number2: "))
     return num1, num2, op(num1, num2)
while True:
     op = input("Input operater ('+','-','*','/','%','end'): ")
     if op == '+':
          num1, num2, ret = arithmetic_ops(sum)
     elif op == '-':
          num1, num2, ret = arithmetic_ops(sub)
     elif op == '*':
          num1, num2, ret = arithmetic_ops(lambda x, y: x*y)
     elif op == '/':
          num1, num2, ret = arithmetic_ops(lambda x, y: x/y)
     elif op == '%':
          num1, num2, ret = arithmetic_ops(lambda x, y: x%y)
     elif op == "end":
          break
     else:
          print("Invalid operation")
          continue
     print(f"{num1} {op} {num2} = {ret}")
print("프로그램 종료")