print("*****************STREAM SELECTION*****************")

print("chose subject form(Math, Physics, Chemistry, Graphics, Programming, Biology, Circuits,Ai ,Robot )")

sub1 = input("enter first favourite subject you like :")
sub2 = input("enter second favourite subject you like :")
ns1 = sub1.capitalize()
ns2 = sub2.capitalize()

print(ns1, ns2)

if(ns1 == "Math" and ns2 == "Physics"):
    print("your ideal branch is mechanical engineering")
elif(ns1 == "Math" and ns2 == "Programming"):
    print("your ideal branch is Computer science")
elif(ns1 == "Biology" and ns2 == "Programming"):
    print("your ideal branch is Biotechnology")
elif(ns1 == "Math" and ns2 == "Circuits"):
    print("your ideal branch is E")

