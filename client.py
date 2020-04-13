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

refreshed = False
boardSelection = "nill"
url = "https://cyberland2.club/"

print("sm0lman's cringe cyberland.club python client")
print(" ")
print("Please select the board you wish to view")
print("/t/")
print("/o/")
print("/n/")
print("/i/")
boardSelection = input("Selection: ")

def boardFetch():
    print("Fetching",boardSelection+"...")
    board = requests.get(url+boardSelection+"?num=50")
    posts = json.loads(board.content)
    posts = list(reversed(posts))
    for post in range(1,len(posts)):
        print("\n================================================")
        print("Post ID: "+ str(posts[post]['id']) + " | Time: "+ posts[post]['time'])
        if posts[post]['replyTo'] != "0" and type(posts[post]['replyTo']) is str:
            print(">>" + posts[post]['replyTo'])
        print("================================================")
        print(posts[post]['content'])
        print("================================================\n")

def menu():
    print("[N]ew OP Post, [F]ollow a thread, [R]eply to a thread, Refresh [B]oard, Refresh [T]hread, [C]hange board,[S]end ANSI image, [Q]uit") 
    menuChoice = str(input("Select a choice: "))
    return menuChoice


while True:
    if refreshed == False:
       boardFetch()
    refreshed = False
    menuChoice = menu()

    if menuChoice.lower() == "n":
        message = input("What message?: ")
        r = requests.post(url+boardSelection, data={"content":message,"replyTo":"null"})
        print(r)

    elif menuChoice.lower() == "f":
        threadNumber = input("Please choose a thread to view: ")
        os.system('clear')
        thread = requests.get(url+boardSelection+"?thread="+threadNumber+"&num=50")
        posts = json.loads(thread.content)
        posts = list(reversed(posts))
        for post in range(1,len(posts)):
            print("Post ID: "+ str(posts[post]['id']))
            if type(posts[post]['replyTo']) is str:
                if posts[post]['replyTo'] != "0":
                    print("In Reply To: " + posts[post]['replyTo'])
            print("Post Content:")
            print(posts[post]['content'])
            print("==========================")

        input("Press enter to continue...")
        os.system("clear")

    elif menuChoice.lower() == "r":
        replyTo = input("Please choose a thread number to reply to: ")
        message = input("Please choose a message: ")
        r = requests.post(url+boardSelection, data={"content":message,"replyTo":replyTo})
        print(r)

    elif menuChoice.lower() == "b":
        os.system("clear")
        boardFetch()
        refreshed = True

    elif menuChoice.lower() == "t":
        os.system('clear')
        thread = requests.get(url+boardSelection+"?thread="+threadNumber+"&num=50")
        prettyThread = json.dumps(thread.json(), indent=4)
        print(prettyThread)

    elif menuChoice.lower() == "c":
        print("Boards to change to: ")
        print("/t/")
        print("/o/")
        print("/n/")
        print("/i/")
        boardSelection = input("Selection: ")

    elif menuChoice.lower() == "s":
        ansFileName = input("Please give the name of the ANSI file you want to send: ")
        print("Sending ANSI file...")
        ansiFile = open(ansFileName, "r")
        message = input("Insert a message to put alongside your image: ")
        r = requests.post(url+boardSelection, data={"content":(message + "\n" + ansiFile.read()),"replyTo":"null"})
        print(r)
        
    elif menuChoice.lower() == "q":
        print("Quitting! Bye Bye...")
        quit()
        
    else:
      print("An error occured...")
