import sys 
import random

room = {}
word = "yes"

def esc() :
    global room
    print("you escaped the dungeon you get 50 points")
    room = outside
def change_room() :
    global room
    print("you go outside")
    room = outside
def attack() :
    print("you do some damage")
souls = {
    "jump": "you jumped " + str(random.randint(6,20)) + " inches"
}
dungeon = {
    "commands": {
        "esc": esc,
        "change": change_room
    },
    "description": "you are in a dungeon you have a broadsword a dirk and some armor what do you do",
    "inventory": [
        "ladder",
        "rats",
        "rusty old sword"
    ]
}

outside = {
    "commands": {
        "attack": attack
    },
    "description": "you are now in a forest",
    "inventory": [
        "scary monster"
    ]
}

room = dungeon

sass = [
    "Whatchoo talkin' 'bout, foo?",
    "Speak English, child!",
    "Shut up!",
    "Huh??",
    "How about no.",
    "How about I {0} your face!",
    "That's not my job, I'm just the narrator!",
    "That ain't right!"
]

while True:
    print()
    print(room["description"])
    print("things you see here: " + ", ".join(room["inventory"]))
    command = sys.stdin.readline().strip()
    words = command.split(' ')
    verb = words[0]
    if verb in souls:
        print(souls[verb])
    elif verb in room["commands"]:
        room["commands"][verb]()
    else:
        s = sass[random.randint(0, len(sass) - 1)]
        s = s.format (command)
        print(command + "? " + s)

# print random.random()

