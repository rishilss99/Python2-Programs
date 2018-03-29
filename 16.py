#Some timepass
print "Hello,Welcome to the login page of noob online\nPlease select from one of the below given options"
print "1.Sign in\n2.Sign up"
a = int(raw_input("Enter your choice:"))
while(a!=1 and a!=2):
    print "Invalid input"
    a = int(raw_input("Enter your choice:"))
database={"rishil":["ilovemyself","Rishil Shah"],"dan":["shutup","Dan Bilzerian"]}
if a==1:
    userenter=raw_input("Enter username:")
    passenter=raw_input("Enter password:")
    while(passenter!=database[userenter][0]):
        passenter=raw_input("Re-enter password:")
    else:
        print "Password matched\nHello %s"%(database[userenter][1])

elif a==2:
    namestore=raw_input("Enter your name:")
    userstore=raw_input("Enter a username:")
    passstore=raw_input("Enter a password:")
    database[userstore]=[passstore,namestore]
