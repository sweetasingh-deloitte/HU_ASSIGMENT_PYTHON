class FormulaError(Exception): pass

def cal_input(user_input):

  input_list=user_input.split()
  if len(input_list)!= 3:
    raise FormulaError('Input does not consist three elements')
  n1,oper,n2= input_list
  try:
    n1 = float(n1)
    n2 = float(n2)
  except ValueError:
    raise FormulaError('The first and third value should be numbers')
  return n1, oper, n2


def calculate(n1, oper, n2):

  if oper == '+':
    return n1 + n2
  if oper == '-':
    return n1 - n2
  if oper == '*':
    return n1 * n2
  if oper == '/':
    return n1 / n2
  raise FormulaError(oper + ' is not a valid operator')


while True:
  user_input = input('Enter operation: ')
  if user_input == 'quit':
    break
  n1, oper, n2 = cal_input(user_input)
  result = calculate(n1, oper, n2)
  print(result)