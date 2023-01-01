def divided_by(a, b):
    return a/b
try:
  print(divided_by(40,0))
except ZeroDivisionError as e:
  print(e,'we can not divide by zero!')