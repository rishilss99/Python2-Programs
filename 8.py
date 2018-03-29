#Just some time pass
#I will be learning lists slicing and appending

family = ["Grandfather" , "Grandmother" , "Father" , "Mother" , "Son"]
print "So this is basically a family of %d members who are %s" % ( len(family) ,family )

add = raw_input("So you are ? :")
family.append(add)
print "So now the family has %d members who are %s" % (len(family) , family)
print "Well I love everyone %s" % (family[:4])
index = family.index("Son")
family.insert(index , "Daughter")
print "The one at index %d who is the %s is the most irritating" % (index , family[index])
family.sort()
for member in family:
    print "I love %s" % (member)
