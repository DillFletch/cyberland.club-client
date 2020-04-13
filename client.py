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

url = "https://cyberland2.club/"

print("sm0lman's cringe cyberland.club python client")
print(" ")
print("Please select the board you wish to view")
print("/t/")
print("/o/")
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
    print("6. Change board")
    print("7. Exit")
    menuChoice = int(input("Select a choice: "))

    if menuChoice == 1:
        message = input("Please choose a message: ")
        r = requests.post(url+boardSelection, data={"content":message,"replyTo":"null"})
        print(r)

    elif menuChoice == 2:
        threadNumber = input("Please choose a thread to view: ")
        os.system("clear")
        thread = requests.get(url+boardSelection+"?thread="+threadNumber+"&num=200")
        prettyThread = json.dumps(thread.json(), indent=4)
        print(prettyThread)

    elif menuChoice == 3:
        replyTo = input("Please choose a thread number to reply to: ")
        message = input("Please choose a message: ")
        r = requests.post(url+boardSelection, data={"content":message,"replyTo":replyTo})
        print(r)

    elif menuChoice == 4:
        os.system("clear")
        boardFetch()

    elif menuChoice == 5:
        os.system("clear")
        thread = requests.get(url+boardSelection+"?thread="+threadNumber+"&num=20")
        prettyThread = json.dumps(thread.json(), indent=4)
        print(prettyThread)

    elif menuChoice == 6:
        print("Boards to change to: ")
        print("/t/")
        print("/o/")
        print("/n/")
        boardSelection = input("Selection: ")
        return boardSelection

    elif menuChoice == 7:
        print("Quitting! Bye Bye...")
        return "quit"
        
    else:
      print("An error occured...")

def boardFetch(boardSelection):
    print("Fetching",boardSelection+"...")
    board = requests.get(url+boardSelection+"?num=200")
    prettyBoard = json.dumps(board.json(), indent=4)
    print(prettyBoard)
    return menu()


choice = boardFetch(boardSelection)
if (choice == "quit"):
    quit()
else:
    boardFetch(choice)

while True:
    menu()
