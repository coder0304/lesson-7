print("select your ride:")
print("1. Bike")
print("2. car")

choice= int(input("enter your choice:"))

if(choice==1):
    print("what type of bike")
    print("1.scooty\n")
    print("12.scooter\n")

    choice2=int(input("enter your choice:"))
    if choice2==1 :
        print("you have selsected scooty")
    else:
        print("you have selsected scooter")

elif(choice==2):
    print("what type of car  ")
    print("1.sedan\n")
    print("2.XUV")
    choice2=int(input("enter your choice:"))
    if choice2==1 :
        print("you have selsected sedan")
    else:
        print("you have selsected XUV")
