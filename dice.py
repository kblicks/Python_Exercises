import random

print("Welcome to the dice simulator!")

roll = "r"
while (roll != "x"):
    roll = input("Press r to roll or x to quit\n")

    if roll == "r":
        number = random.randint(1, 6)
        if number == 1:
            print("[-----------]")
            print("[           ]")
            print("[     0     ]")
            print("[           ]")
            print("[-----------]")
        elif number == 2:
            print("[-----------]")
            print("[           ]")
            print("[   0   0   ]")
            print("[           ]")
            print("[-----------]")
        elif number == 3:
            print("[-----------]")
            print("[ 0         ]")
            print("[     0     ]")
            print("[         0 ]")
            print("[-----------]")
        elif number == 4:
            print("[-----------]")
            print("[  0     0  ]")
            print("[           ]")
            print("[  0     0  ]")
            print("[-----------]")
        elif number == 5:
            print("[-----------]")
            print("[  0     0  ]")
            print("[     0     ]")
            print("[  0     0  ]")
            print("[-----------]")
        elif number == 6:
            print("[-----------]")
            print("[  0     0  ]")
            print("[  0     0  ]")
            print("[  0     0  ]")
            print("[-----------]")
    elif roll == "x":
        exit("Goodbye!")
    else:
        print("Invalid option")
