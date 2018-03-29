g = int(raw_input())
my=[]
temp = raw_input()
t=len(temp)-1
if t==2:
    for i in range(t + 1):
        if (i != t and i != 0):
            if (temp[i] != ' ' and temp[i + 1] != ' '):
                my.append(int(temp[i:i + 2]))
            elif (temp[i] != ' ' and temp[i + 1] == ' ' and temp[i - 1] == ' '):
                my.append(int(temp[i]))
        elif (i == 0 and temp[i + 1] == ' '):
            my.append(int(temp[0]))
        elif (i == t and temp[t - 1] == ' '):
            my.append(int(temp[t]))
else:
    f=0
    while f<=t:
        if(temp[f]!=' ' and temp[f+2]==' '):
            my.append(int(temp[f:f+2]))
            f+=2
        elif(temp[f]!=' ' and temp[f+3]==' '):
            my.append(int(temp[f:f+3]))
            f+=4
t=tuple(my)
print hash(t)