import os, json, requests, sys

## Check is user has supplied instance URL as an arguement, default to https://cyberland.digital
try:
    if type(sys.argv[1]) is str:
        url = sys.argv[1]
except:
    url = "https://cyberland.digital"


## Get and print relevant ASCII art from top 8 lines of homepage
for line in requests.get(url).text.split("\n")[:8]:
    print(line)

refreshed = False
boardSelection = "nill"

## Initial selection
print("sm0lman's cringe cyberland.club python client\n")
print("Please select the board you wish to view")
print("/t/")
print("/o/")
print("/n/")
print("/i/") ## Will be updated in the future to fetch boards.json and show available boards on instance
boardSelection = input("Selection: ")

## fetch OP posts
def boardFetch(board):
    print("Fetching ",board," OP posts")
    content = requests.get(url+board+"?thread=0").content
    showPosts(content)

## Show posts nicely formatted
def showPosts(content):
    posts = json.loads(content)
    posts = list(reversed(posts))
    for post in range(1,len(posts)):
        print("\n================================================")
        print("Post ID: "+ str(posts[post]['id']) + " | Time: "+ posts[post]['time'])
        if posts[post]['replyTo'] != "0" and type(posts[post]['replyTo']) is str:
            print(">>" + posts[post]['replyTo'])
        else:
            print("OP")
        print("================================================")
        print(posts[post]['content'])
        print("================================================\n")


def showMenu(type):
    if type == "board":
        print("[N]ew OP Post, [F]ollow a thread, [R]eply to a post, Refresh [B]oard, [C]hange board, [S]end ANSI image, [Q]uit") 
    elif type == "thread":
        print("[R]eply to a post, [B]ack to OP posts, [C]hange board, Refresh [T]hread, [S]end ANSI image, [Q]uit")
    menuChoice = str(input("Select a choice: "))
    return menuChoice


while True:
    if refreshed == False: ## Check if it is refreshed
       boardFetch(boardSelection)
    refreshed = False
    menuChoice = showMenu("board")

    if menuChoice.lower() == "n": ## New OP post
        message = input("What message?: ")
        r = requests.post(url+boardSelection, data={"content":message, "replyTo": "0"})
        showPosts(r.content)
        refreshed = True
        print(r.status_code)

    elif menuChoice.lower() == "f": ## Follow thread
        threadNumber = input("Please choose a thread to view: ")
        os.system('clear')
        content = requests.get(url+boardSelection+"?thread="+threadNumber+"&num=50").content
        showPosts(content)
        showMenu("thread")


    elif menuChoice.lower() == "r": ## Reply to thread
        replyTo = input("Please choose a thread number to reply to: ")
        message = input("Please choose a message: ")
        r = requests.post(url+boardSelection, data={"content":message,"replyTo":replyTo})
        print(r.status_code)

    elif menuChoice.lower() == "b": ## Refresh board
        os.system("clear")
        boardFetch(boardSelection)
        refreshed = True

    elif menuChoice.lower() == "t": ## Refresh thread
        os.system('clear')
        content = requests.get(url+boardSelection+"?thread="+threadNumber+"&num=50").content
        showPosts(content)

    elif menuChoice.lower() == "c": ## Change board
        print("Boards to change to: ")
        print("/t/")
        print("/o/")
        print("/n/")
        print("/i/")
        boardSelection = input("Selection: ")

    elif menuChoice.lower() == "s": ## Send ASCII
        ansFileName = input("Please give the name of the ANSI file you want to send: ")
        print("Sending ANSI file...")
        ansiFile = open(ansFileName, "r")
        message = input("Insert a message to put alongside your image: ")
        r = requests.post(url+boardSelection, data={"content":(message + "\n" + ansiFile.read())})
        print(r.status_code)
        
    elif menuChoice.lower() == "q": ## Quit
        print("Quitting! Bye Bye...")
        quit()
        
    else:
      print("An error occured...")