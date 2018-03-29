#Magic Trick
from random import randint
print "Welcome to my show !!\nNow for today's magic trick"
rand = randint(1000,100000)
print "Well here's a random number %d" % rand
print "You and I are gonna play with some numbers now"
my1 = randint(1000,2000)
print "So I say %d" % my1
your1 = int(raw_input("Say a number with digits 1-9 and none repeated:"))
print "So you say %d" % your1
sum1 = my1 + your1
diff1 = rand - sum1







