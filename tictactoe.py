import random
ccounter = 0
l,vmpos = [[" ", "|", " ", "|", " "],["-", "+", "-", "+", "-"],[" ", "|", " ", "|", " "],["-", "+", "-", "+", "-"],[" ", "|", " ", "|", " "]],[0,1,2,3,4,5,6,7,8]
lineNumber=0
def goto(line):
    global lineNumber
    line = lineNumber

def draw_board():
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j],end="")
        print()
    return

def next_move():
    global ccounter
    if(ccounter % 2 == 0):
        print("enter the place for your next move")
        nm=int(input())
        if(nm in vmpos):
            del vmpos[vmpos.index(nm)]
            move(nm)
            ccounter=ccounter+1
        else:
            print("invalid position")
            goto(24)
    else:
        print("computer turn")
        a=random.choice(vmpos)
        move(a)
        del vmpos[vmpos.index(a)]
        ccounter=ccounter+1
    if(outcome_eval()):
        return
    else:
        next_move()
    return

def outcome_eval():
    if(l[0][0]==l[0][2]==l[0][4]!=" " or l[2][0]==l[2][2]==l[2][4]!=" " or l[4][0]==l[4][2]==l[4][4]!=" " or l[0][0]==l[2][0]==l[4][0]!=" " or l[0][2]==l[2][2]==l[4][2]!=" " or l[0][4]==l[2][4]==l[4][4]!=" " or l[0][0]==l[2][2]==l[4][4]!=" " or l[0][4]==l[2][2]==l[4][0]!=" "):
        return 1
    else:
        return 0

def move(nm):
    a,b = 0,0
    if (nm == 0):        a,b = 0,0
    if (nm == 1):        a,b = 0,2
    if (nm == 2):        a,b = 0,4
    if (nm == 3):        a,b = 2,0
    if (nm == 4):        a,b = 2,2
    if (nm == 5):        a,b = 2,4
    if (nm == 6):        a,b = 4,0
    if (nm == 7):        a,b = 4,2
    if (nm == 8):        a,b = 4,4
    if (ccounter % 2 == 0):
        l[a][b]="X"
        draw_board()
    else:
        l[a][b]="O"
        draw_board()
    return
draw_board()
next_move()