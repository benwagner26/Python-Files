import random

class gameOfSevens(object):
    def __init__(self):
        self.balance = 0
    

    def greeting(self):
        name = input("Enter your name: ")
        self.user = name
        print(f"Hi {self.user}! Welcome to the game of lucky 7's")


    def setBalance(self):
        pot = int(input("How much would would you like to bet: "))
        self.balance = pot

    
    def getBalance(self):
        return self.balance


    def play(self):
        print("Enter the type of play")
        manaully = input("For Manual Roll Press [M/m]\nFor Auto Roll Press [Enter]:  ")
        print("")
        print("")
        if (manaully == "M" or manaully == "m"):
            self.manualGame()
        else:
            self.autoGame()


    def autoGame(self):
        
        self.greeting()
        self.setBalance()
        
        num_of_rolls = 0
        
        while (self.getBalance() > 0):
            print("-----------------------------")
            print("\t\t\tBalance: ", self.getBalance())
            num_of_rolls += 1
            dice1 = random.randint(1,7)
            dice2 = random.randint(1,7)
            print("You rolled a ", dice1, " and a ", dice2)
            if ((dice1 + dice2) == 7):
                self.balance += 4
            else:
                self.balance -= 1

        
        print("")
        print("")
        print ("You loose")
        print("It took ", num_of_rolls, " to break you")
        print("")
        print("")
        play_again = input("Would you like to play again press [Y/y]:  ")
        print("")
        print("")
        if (play_again == "Y" or play_again == "y"):
            manaully = input("For Manual Roll Press [M/m]\nFor Auto Roll Press [Enter]:  ")
            print("")
            print("")
            if (manaully == "M" or manaully == "m"):
                self.manualGame()
            else:
                self.autoGame()
        else:
            print("Come back again when you got the cash")


    def manualGame(self): 
        
        self.greeting()
        self.setBalance()
        
        num_of_rolls = 0
        print("[INSTRUCTIONS] Press ENTER to Roll")
        while (self.getBalance() > 0):
            input()
            print("-----------------------------")
            print("\t\t\tBalance: ", self.getBalance())
            num_of_rolls += 1
            dice1 = random.randint(1,7)
            dice2 = random.randint(1,7)
            print("You rolled a ", dice1, " and a ", dice2)
            if ((dice1 + dice2) == 7):
                self.balance += 4
            else:
                self.balance -= 1

        
        print("")
        print("")
        print ("You loose")
        print("It took ", num_of_rolls, " to break you")
        print("")
        print("")
        play_again = input("Would you like to play again press [Y/y]:  ")
        print("")
        print("")
        if (play_again == "Y" or play_again == "y"):
            manaully = input("For Manual Roll Press [M/m]\nFor Auto Roll Press [Enter]:  ")
            print("")
            print("")
            if (manaully == "M" or manaully == "m"):
                self.manualGame()
            else:
                self.autoGame()
        else:
            print("Come back again when you got the cash")
    

game = gameOfSevens()

game.play()