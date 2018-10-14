from random import *
import shifter as s
counter = 0
trash = []

class user():
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

def init():
    pad = open("words.txt", "r")
    lines = pad.readlines()
    guess = ""
    global hidden
    hidden = lines[randint(0,len(lines))].lower()
    global shown
    shown = []
    for i in range (len(hidden) - 1):
            shown += "*"
def checker(guess,trash):
    a = 0
    if guess.lower() in hidden.lower():
        if guess not in trash:
            for i in range (len(hidden)):
                if hidden[i] == guess:
                    shown[i] = hidden[i]
                    a+=1
            trash += guess
            return a
            
    else:
        print("Wrong")
        return 0


def createUser():
    newUser = user(input("Enter a username: "), input("Enter a password: "))
    confirmed = input("Confirm password :")
    while confirmed != newUser.password:
        newUser.password = input("Please re-enter password: ")
    userFileName = newUser.username
    userFile = open(userFileName+".txt","w+")
    s.encrypt((","+newUser.username+","),userFile)
    s.encrypt((","+newUser.password+","),userFile)


    
init()
while True:
        createUser()
        print(hidden)
        print(''.join(shown))
        counter += checker(input("\nEnter a letter: "),trash)
        print(counter)
        if counter == (len(hidden)-1):
            print("\nWinrar!\n")


""""    
|--------
|       |
|       | "why me!"
|       |   /
|       o 
|      /|\ 
|     / | \
|       |
|      | |
|      | |
|      
|
|_____________
"""""
