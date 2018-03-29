#Timepass
a = int(raw_input("Enter:"))
b = range(1,a+1)
for i in range(len(b)):
    b[i] = str(b[i])
print "".join(b)
