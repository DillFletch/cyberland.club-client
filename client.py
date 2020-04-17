import os, json, requests, sys

def chooseBoard():
    print("Please select the board you wish to view")
    print("/t/")
    print("/o/")
    print("/n/")
    print("/i/") ## Will be updated in the future to fetch boards.json and show available boards on instance when implemented into cyberland protocol
    return input("Selection: ")

## fetch OP posts
def OPFetch(board):
    print("Fetching ",board," OP posts")
    content = requests.get(url+board+"?thread=0").content
    showPosts(content)
    return showMenu('board')

## Fetch posts from a thread
def threadFetch(board, thread):
    print("Fetching replies to post "+thread+" on board "+board)
    content = requests.get(url+board+"?thread="+thread).content
    showPosts(content)
    return showMenu('thread')

## Show posts nicely formatted
def showPosts(content):
    clearScreen()
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

## Clears the screen, with a different method based on which OS is being run.
def clearScreen():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
   
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

    ## Initial selection
    print("sm0lman's cyberland python client\n")
    boardSelection = chooseBoard()
    menuChoice = OPFetch(boardSelection)
    refreshed = True

    while True:
        if refreshed == False: ## Check if it is refreshed
            menuChoice = OPFetch(boardSelection)
        refreshed = False

        if menuChoice.lower() == "n": ## New OP post
            message = input("What message?: ")
            r = requests.post(url+boardSelection, data={"content":message, "replyTo": "0"})
            showPosts(r.content)
            refreshed = True
            print(r.status_code)

        elif menuChoice.lower() == "f": ## Follow thread
            threadNumber = input("Please choose a thread to view: ")
            menuChoice = threadFetch(boardSelection, threadNumber)
            refreshed = True


        elif menuChoice.lower() == "r": ## Reply to thread
            replyTo = input("Please choose a thread number to reply to: ")
            message = input("Please choose a message: ")
            r = requests.post(url+boardSelection, data={"content":message,"replyTo":replyTo})
            print(r.status_code)
            menuChoice = threadFetch(boardSelection, replyTo)
            refreshed = True

        elif menuChoice.lower() == "b": ## Refresh board
            clearScreen()
            menuChoice = OPFetch(boardSelection)
            refreshed = True

        elif menuChoice.lower() == "t": ## Refresh thread
            clearScreen()
            menuChoice = threadFetch(boardSelection, threadNumber)
            refreshed = True

        elif menuChoice.lower() == "c": ## Change board
            boardSelection = chooseBoard()

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