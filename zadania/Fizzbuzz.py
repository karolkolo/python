

for x in range(1,101):
  if (x % 3 == 0) and (x % 5 == 0):
    x = "Fizzbuzz"
  elif (x % 3 == 0):
    x = "Fizz"
  elif (x % 5 ==0):
    x = "Buzz"
  print(x)
