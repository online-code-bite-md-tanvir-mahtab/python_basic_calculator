from art import logo
from replit import clear
print(logo)


# Addition
def add(n1,n2):
  return n1 + n2

# substraction

def sub(n1,n2):
  return n1 - n2

# Multiplication
def mul(n1,n2):
  return n1*n2

# divition
def div(n1,n2):
  return n1/n2

# Calculator
def calculation():
  clear()
  choose  = True
  # creting the symbol list
  arr_of_symbol = ['+','-','*','/']
  n1 = int(input("What's the first number?:"))
  for symbol in arr_of_symbol:
    print(symbol)
  while choose:
    result = 0
    if int(n1) == ' ':
      choose = False
    else:
      pic_the_oparation = input("Pick on the operation ? :")
      if pic_the_oparation !=' ':
        n2 = int(input("What's the next number?:"))
        if pic_the_oparation == '+':
          result = add(n1,n2)
        elif pic_the_oparation == '-':
          result = sub(n1,n2)
        elif pic_the_oparation == '*':
          result = mul(n1,n2)
        elif pic_the_oparation == '/':
          result = div(n1,n2)
        print(f"{n1} {pic_the_oparation} {n2} = {result}")
        excution = input("Enter 'Yes' to calculate  'again' to calculat new or  'No' to exit ?").lower()
        if excution == "yes":
          # now i am going to store the result as the n1 value
          n1 = int(result)
          choose = True
        elif excution == "again":
          calculation()
        else:
          choose= False


if __name__ == "__main__":
  calculation()