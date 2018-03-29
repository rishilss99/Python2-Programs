from string import maketrans
given = "Hey there ducker how you doing mofo"
print given.find("sucks")
transtab=maketrans("aeiou","12345")
print given.translate(transtab)
print given.replace("h","i")
t="pozwbtpyvoyrsseuwojzvehnvvygrkib"
new=""
for i in t:
    new = new + str((int(i)+26)%65)
print new