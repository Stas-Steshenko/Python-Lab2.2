from mod import factorial

def expression (x, y):
  if x > 8:
      z = 3 + y
      return z
  else:
      z = 9 * x * y
      return z

x = int(input("Введіть значення x: "))
y = int(input("Введіть значення y: "))
print ("Значення виразу z = ", expression(x, y))

n = int(input("Введіть число n: "))
print("Факторіал числа n = ", factorial (n))