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
        print("Post ID: "+ str(posts[post]['id']))
        if posts[post]['replyTo'] is int:
            print("In Reply To: " + posts[post]['replyTo'])
        print("Post Content:")
        print(posts[post]['content'])
        print("==========================")

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
    return menuChoice


while True:
    if refreshed == False:
       boardFetch()
    refreshed = False
    menuChoice = menu()

    if menuChoice == 1:
        message = input("Please choose a message: ")
        r = requests.post(url+boardSelection, data={"content":message,"replyTo":"null"})
        print(r)

    elif menuChoice == 2:
        threadNumber = input("Please choose a thread to view: ")
        os.system('clear')
        thread = requests.get(url+boardSelection+"?thread="+threadNumber+"&num=50")
        posts = json.loads(thread.content)
        posts = list(reversed(array))
        for post in range(1,len(posts)):
            print("Post ID: "+ str(posts[post]['id']))
            if posts[post]['replyTo'] is int:
                print("In Reply To: " + posts[post]['replyTo'])
            print("Post Content:")
            print(posts[post]['content'])
            print("==========================")

        input("Press enter to continue...")
        os.system("clear")

    elif menuChoice == 3:
        replyTo = input("Please choose a thread number to reply to: ")
        message = input("Please choose a message: ")
        r = requests.post(url+boardSelection, data={"content":message,"replyTo":replyTo})
        print(r)

    elif menuChoice == 4:
        os.system("clear")
        boardFetch()
        refreshed = True

    elif menuChoice == 5:
        os.system('clear')
        thread = requests.get(url+boardSelection+"?thread="+threadNumber+"&num=50")
        prettyThread = json.dumps(thread.json(), indent=4)
        print(prettyThread)

    elif menuChoice == 6:
        print("Boards to change to: ")
        print("/t/")
        print("/o/")
        print("/n/")
        print("/i/")
        boardSelection = input("Selection: ")
        
    elif menuChoice == 7:
        print("Quitting! Bye Bye...")
        quit()
        
    else:
      print("An error occured...")
