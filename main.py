def printBoard(xState,yState):
    zero = 'X' if xState[0] else ('o' if yState[0] else 0)
    one = 'X' if xState[1] else ('o' if yState[1] else 1)
    two = 'X' if xState[2] else ('o' if yState[2] else 2)
    three = 'X' if xState[3] else ('o' if yState[3] else 3)
    four = 'X' if xState[4] else ('o' if yState[4] else 4)
    five = 'X' if xState[5] else ('o' if yState[5] else 5)
    six = 'X' if xState[6] else ('o' if yState[6] else 6)
    seven = 'X' if xState[7] else ('o' if yState[7] else 7)
    eight = 'X' if xState[8] else ('o' if yState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")
    pass
xState = [0,0,0,0,0,0,0,0,0]
yState = [0,0,0,0,0,0,0,0,0]
turn=1
print("Welcome to Tic Tac Toe")
while(True):
    printBoard(xState,yState)
    if(turn==1):
        print("X's chance")
        value=int(input("enter a value"))
        xState[value]=1
    else:
        print("Y's chance")
        value=int(input("enter a value"))
        yState[value]=1
    turn = 1-turn

    