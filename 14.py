t = int(raw_input("T:"))
list =[]
for i in range(t):
    n = int(raw_input("N:"))
    list.append(n)
temp = {}
for x in list:
    sub = 0
    for a in range(1,x+1):
        initial = 1
        js = 0
        new = []
        while initial < a:
            if a%initial ==0:
                js = js + initial**2
            else:
                js = js + 1
            initial = initial + 1
        temp[new] = js

print temp

















