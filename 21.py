n=int(raw_input())
for i in range(1,10001):
    t = bin(i)
    sum=0
    for each in range(2,len(t)):
        sum=sum+int(t[each])
    if(sum==n):
        print i






