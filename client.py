import os
import time
import json
import requests

print('''
  ____      _               _                 _       _       _     
 / ___|   _| |__   ___ _ __| | __ _ _ __   __| |  ___| |_   _| |__  
| |  | | | | '_ \ / _ \ '__| |/ _` | '_ \ / _` | / __| | | | | '_ \ 
| |__| |_| | |_) |  __/ |  | | (_| | | | | (_| || (__| | |_| | |_) |
 \____\__, |_.__/ \___|_|  |_|\__,_|_| |_|\__,_(_)___|_|\__,_|_.__/ 
      |___/                                                         

        ''')

print("sm0lman's cringe cyberland.club python client")
print(" ")
print("Please select the board you wish to view")
print("/o/")
print("/t/")
print("/n/")
boardSelection = input("Selection: ")

def menu():
    print(" ")
    print("What would you like to do now?")
    print("1. Make a post with no reply")
    print("2. View all replys to a thread")
    print("3. Reply to a thread")
    print("4. Refresh board")
    print("5. Refresh thread")
    print("6. Exit")
    menuChoice = int(input("Select a choice: "))

    if menuChoice == 1:
        message = input("Please choose a message: ")
        r = requests.post("https://cyberland.club"+boardSelection, data={"content":message,"replyTo":"null"})
        print(r)

    elif menuChoice == 2:
        threadNumber = input("Please choose a thread to view: ")
        os.system("clear")
        thread = requests.get("https://cyberland.club"+boardSelection+"?thread="+threadNumber+"&num=20")
        prettyThread = json.dumps(thread.json(), indent=4)
        print(prettyThread)

    elif menuChoice == 3:
        replyTo = input("Please choose a thread number to reply to: ")
        message = input("Please choose a message: ")
        r = requests.post("https://cyberland.club"+boardSelection, data={"content":message,"replyTo":replyTo})
        print(r)

    elif menuChoice == 4:
        os.system("clear")
        boardFetch()

    elif menuChoice == 5:
        os.system("clear")
        thread = requests.get("https://cyberland.club"+boardSelection+"?thread="+threadNumber+"&num=20")
        prettyThread = json.dumps(thread.json(), indent=4)
        print(prettyThread)

    elif menuChoice == 6:
        print("Quitting! Bye Bye...")
        quit()
        
    else:
      print("An error occured...")

def boardFetch():
    print("Fetching",boardSelection+"...")
    board = requests.get("https://cyberland.club"+boardSelection+"?num=20")
    prettyBoard = json.dumps(board.json(), indent=4)
    print(prettyBoard)
    menu()



boardFetch()

while True:
    menu()
