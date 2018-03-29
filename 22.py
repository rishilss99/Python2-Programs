n=int(raw_input())
array=map(int,raw_input().split())
print array
pos=[]
neg=[]
zero=[]
for t in array:
    if t>0:
        pos.append(t)
    elif t<0:
        neg.append(t)
    elif t==0:
        zero.append(t)
if len(zero)==0 or len(neg)==0:
    print "No solution"
elif len(pos)==0:
    if len(neg)>=3 and len(neg)%2!=0:
        pos.append(neg[0])
        pos.append(neg[1])
        neg.pop(0)
        neg.pop(1)
        print len(pos), " ".join(map(str, pos))
        print len(neg), " ".join(map(str, neg))
        print len(zero), " ".join(map(str, zero))
    elif len(neg)>=3 and len(neg)%2==0:
        pos.append(neg[0])
        pos.append(neg[1])
        neg.pop(0)
        neg.pop(1)
        zero.append(neg[0])
        neg.pop(0)
        print len(pos), " ".join(map(str, pos))
        print len(neg), " ".join(map(str, neg))
        print len(zero), " ".join(map(str, zero))
    else:
        print "No solution"
elif len(pos)>0 and len(neg)%2==0:
    zero.append(neg[0])
    neg.pop(0)
    print len(pos), " ".join(map(str, pos))
    print len(neg), " ".join(map(str, neg))
    print len(zero), " ".join(map(str, zero))
else:
    print len(pos)," ".join(map(str,pos))
    print len(neg), " ".join(map(str,neg))
    print len(zero), " ".join(map(str,zero))