#Iteration of a list
n=[1,4,5]
for i in range(len(n)):
    print n[i]

board = []
for i in range(5):
    board.append(["O"]*5)

for x in board:
    print " ".join(x)

a = raw_input("Number")
a = int(a)
print a * 10
from random import randint
rate_me = randint(0,10)
print "I rate you : %d" % rate_me

print range(5)