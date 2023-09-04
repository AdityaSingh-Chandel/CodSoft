import random
L=["Rock","Paper","Scissor"]

while True:
    YourCount=0
    ComputerCount=0
    Initial_Input=int(input("""
                 Rock-Paper-Scissor GAME
                 1- START
                 2- EXIT  
                         """))
    if Initial_Input==1:
        n=int(input("Enter number of rounds: "))
        
        for i in range (n):
            YouInput=int(input("""
                         1-Rock
                         2-Paper
                         3-Scissor 
                              """))
            
            if YouInput==1:
                YourChoice="Rock"
            elif YouInput==2:
                YourChoice="Paper"
            elif YouInput==3:
                YourChoice="Scissor"
            else:
                print("invalid number selected")
                
            ComputerChoice=random.choice(L)
            
            if YourChoice==ComputerChoice:
                print("You chose:",YourChoice)
                print("Computer chose:", ComputerChoice)
                print("Game DRAW")
                print()
            elif (ComputerChoice=="Rock" and YourChoice=="Scissor") or (ComputerChoice=="Paper" and YourChoice=="Rock") or (ComputerChoice=="Scissor" and YourChoice=="Paper"):
                print("You chose:",YourChoice)
                print("Computer chose:", ComputerChoice)
                print("COMPUTER WON")
                print()
                ComputerCount+=1
            else:
                print("You chose:",YourChoice)
                print("Computer chose:", ComputerChoice)
                print("You WON")
                YourCount+=1
                print()
        if YourCount==ComputerCount:
            print("---------FINAL RESULT DECLARATION---------")
            print("Your total score: ",YourCount)
            print("Computer total score: ",ComputerCount)
            print()
            print("Final Result: DRAW ")
        elif YourCount<ComputerCount:
            print("---------FINAL RESULT DECLARATION---------")
            print("Your total score: ",YourCount)
            print("Computer total score: ",ComputerCount)
            print()
            print("Final Result: COMPUTER WON ")
        else:
            print("---------FINAL RESULT DECLARATION---------")
            print("Your total score: ",YourCount)
            print("Computer's total score: ",ComputerCount)
            print()
            print("Final Result: YOU WON ")
            print("Congratulations!....")
    else:
        break        
    