def changeDir(Dir):
    return (Dir + 1) % 4

def calcStatus():
    global status
    global HorKabe
    global VerKabe
    global dirR
    global dirD
    global dirL
    global dirU
    Dir = status[2]
    if Dir == dirR:
        if status[0] == 4:
            status[2] = changeDir(Dir)
        elif HorKabe[status[1]][status[0]] == 1:
            status[0] += 1
        else:
            status[2] = changeDir(Dir)
    elif Dir == dirD:
        if status[1] == 4:
            status[2] = changeDir(Dir)
        elif VerKabe[status[0]][status[1]] == 1:
            status[1] += 1
        else:
            status[2] = changeDir(Dir)
    elif Dir == dirL:
        if status[0] == 0:
            status[2] = changeDir(Dir)
        elif HorKabe[status[1]][status[0] - 1] == 1:
            status[0] -= 1
        else:
            status[2] = changeDir(Dir)
    elif Dir == dirU:
        if status[1] == 0:
            status[2] = changeDir(Dir)
        elif VerKabe[status[0]][status[1] - 1] == 1:
            status[1] -= 1
        else:
            status[2] = changeDir(Dir)
