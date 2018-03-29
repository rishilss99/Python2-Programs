#loops
Dict = ["Apple","Banana","Tomato" , "Guava"]
for item in Dict:
  if item == "Tomato":
    print "Tomato isn't a fruit"
  else:
    print "A",item
else:
  print "Good fruits"

def is_int(x):
    if float(x) - int(x) != 0:
        return False
    else:
        return True

#It's for codecademy

def factorial(x):
    total = 1
    for i in range(1,x + 1):
        total = total*i
    return total

print(factorial(4))





