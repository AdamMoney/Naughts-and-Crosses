def test():
    winlist = []
    global counter
    while counter != 1:
        if ((len(xlist) - len(olist)) >= 2) or ((len(olist) - len(xlist)) >= 2):
            print("Impossible")
            break
        if ((current_state[0] == current_state[1] == current_state[2]) and current_state[0] != "_"):
            winlist.append(current_state[0]) # Horizontal 1
        if ((current_state[3] == current_state[4] == current_state[5]) and current_state[3] != "_"):
            winlist.append(current_state[3])  # Horizontal 2
        if ((current_state[6] == current_state[7] == current_state[8]) and current_state[6] != "_"):
            winlist.append(current_state[6]) # Horizontal 3
        if ((current_state[0] == current_state[3] == current_state[6]) and current_state[0] != "_"):
            winlist.append(current_state[0]) # Vertical 1
        if ((current_state[1] == current_state[4] == current_state[7]) and current_state[1] != "_"):
            winlist.append(current_state[1])  # Vertical 2
        if ((current_state[2] == current_state[5] == current_state[8]) and current_state[2] != "_"):
            winlist.append(current_state[2]) # Vertical 3
        if ((current_state[0] == current_state[4] == current_state[8]) and current_state[0] != "_"):
            winlist.append(current_state[0])  # Diagonal 1
        if ((current_state[2] == current_state[4] == current_state[6]) and current_state[2] != "_"):
            winlist.append(current_state[2])  # Diagonal 2
        if 0<(len(winlist))<2:
            field()
            print(f"{winlist[0]} wins")
            counter = 100
            break
        elif (len(winlist))>=2:
            print("Impossible")
            break
        elif (("_" or " ") in current_state):
            break
        else:
            field()
            print("Draw")
            counter = 100
            break

counter = 0
list = []
winlist = []
#                           O_OXXO_XX
# _XXOO__O_     test
# XOXOXOXXO     X WINS
# XOOOXOXXO     O WINS
# XOXOOXXXO     DRAW
# XO_OOX_X_     GAME NOT FINISHED
# XO_XO_XOX     IMPOSSIBLE
# _O_X__X_X     IMPOSSIBLE
# _OOOO_X_X     IMPOSSIBLE

current_state = []
first = "_________"
current_state = [ch for ch in first]

xlist = [ch for ch in first if ch == "X"]
olist = [ch for ch in first if ch == "O"]

coord_counter = 0
def coordinates():
    global coord_counter
    global game_letter
    while coord_counter !=9:
        print("Enter the coordinates:")
        if (coord_counter%2 == 0):
            game_letter = "X"
        else:
            game_letter = "O"
        x, y = (input().split())
        if (x.isnumeric() and y.isnumeric()):
            if (x == "1" or x == "2" or x == "3") and (y == "1" or y == "2" or y == "3"):
                if (x == "1" and y == "3" and current_state[0] == "_"): # These need to be in "" - doesn't work if integers!
                    current_state[0] = game_letter  # Test = _XXOO_OX_
                    coord_counter +=1
                    break
                if (x == "1" and y == "2" and current_state[3] == "_"):
                    current_state[3] = game_letter
                    coord_counter +=1
                    break
                if (x == "1" and y == "1" and current_state[6] == "_"):
                    current_state[6] = game_letter
                    coord_counter +=1
                    break
                if (x == "2" and y == "3" and current_state[1] == "_"):
                    current_state[1] = game_letter
                    coord_counter +=1
                    break
                if (x == "2" and y == "2" and current_state[4] == "_"):
                    current_state[4] = game_letter
                    coord_counter +=1
                    break
                if (x == "2" and y == "1" and current_state[7] == "_"):
                    current_state[7] = game_letter
                    coord_counter +=1
                    break
                if (x == "3" and y == "3" and current_state[2] == "_"):
                    current_state[2] = game_letter
                    coord_counter +=1
                    break
                if (x == "3" and y == "2" and current_state[5] == "_"):
                    current_state[5] = game_letter
                    coord_counter +=1
                    break
                if (x == "3" and y == "1" and current_state[8] == "_"):
                    current_state[8] = game_letter
                    coord_counter +=1
                    break
                else:
                    print("This cell is occupied! Choose another one!")

            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")



def field():
    print("---------")
    print("|", current_state[0], current_state[1], current_state[2], "|")
    print("|", current_state[3], current_state[4], current_state[5], "|")
    print("|", current_state[6], current_state[7], current_state[8], "|")
    # | O _ O |
    # | X X O |
    # | _ X X |
    print("---------")

game_letter = "X"

while counter != 100:
    field()
    coordinates()
    test()
