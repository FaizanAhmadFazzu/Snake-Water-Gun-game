import random
mylist = ["Snake","Water","Gun"]
gamerounds =["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth"]
i=0
comscore = 0
userscore = 0
while(i<gamerounds.__len__()):
     comchoice = random.choice(mylist)
     print(f"{gamerounds[i]} Round : \n Press S to choose Snake : \nPress W to choose Water :\nPress  G to choose Gun :")
     userchoice  =  input().upper()
     if userchoice == "S" and comchoice == "Water":
         userscore = userscore + 10
         print("You win 10 points\ncomputer choice is",comchoice)
         print("your score is ",userscore)
     elif userchoice == "W" and comchoice == "Snake":
         comscore = comscore + 10
         print("you loose \n computerchoice is ",comchoice)
         print("your score is ", userscore)
     elif userchoice == "G" and comchoice == "Snake":
         userscore = userscore +10
         print("You win 10 points\ncomputer choice is", comchoice)
         print("your score is ", userscore)
     elif userchoice == "S" and comchoice == "Gun":
         print("You loose\ncomputerchoice is ", comchoice)
         comscore = comscore + 10
         print("your score is ", userscore)
     elif userchoice == "W" and comchoice == "Gun":
         userscore = userscore + 10
         print("You win 10 points\ncomputer choice is", comchoice)
         print("your score is ", userscore)
     elif userchoice == "G" and comchoice == "Water":
         print("You loose\n computerchoice is ", comchoice)
         comscore = comscore + 10
         print("your score is ", userscore)
     elif userchoice == "G" and comchoice == "Gun" or userchoice == "W" and comchoice == "Water" or userchoice == "S" and comchoice == "Snake":
         print(" TIE \n your choice and computer choice is same :  ", comchoice)
     else:
         print("Invalid Input")
         i=i-1

     i=i+1

if userscore < comscore:
    print(f"Your score is {userscore} and computerscore is {comscore}\nyou lose by {comscore - userscore} points")
elif userscore == comscore:
    print(f"Your score is {userscore} and computerscore is {comscore}\nDRAW")
else:

    print(f"Your score is {userscore} and computerscore is {comscore}\nYou won  by {userscore - comscore} points")
