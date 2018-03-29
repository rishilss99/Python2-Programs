n=int(raw_input())
initial=[]
for i in range(n):
    initial.append(raw_input())
new={}
done=[]
for each in initial:
    for t in each:
        new[t]=each.count(t)
    my=dict.items(new)
    temp=[]
    fuck=""
    for f in my:
        f=list(f)
        temp.append(f[::-1])
        temp.sort()
    for x in temp:
        fuck+=x[1]*x[0]
    print fuck


