import curses
from .data import Temp

# the below world is 50x, 15y
world = """
............X.....................................
.......X.......X.......X.........X...........X....
....X......X...X...X...........X.......C.X...X....
.X......X....b...X...X..X...X..X.....X........X...
...X.....................e.............X....X.....
........h..X......X...............................
..............X......X.........X........X...X.....
..X...X.....X....X......X.........................
............X...X......X.......X....d......X......
....X...X.......X...X.....X...........X......X....
.....X....X.X.....X.....X.....X...X...............
..X.X......X.X..a.......................X.........
...X...X.........X..X.....g.................X.....
..X.X...X..X....X.........X........f..........X...
..................X....................X..........
"""

playerChar = "@"

# window is 15x, 5y
# |=============|
# |             |
# |      @      |
# |             |
# |=============|

windowBorder = """
|=============|
|#############|
|#############|
|#############|
|=============|
"""
maxX = 49
maxY = 14

CHAR_POS = (2, 12)  # x, y tuple
playerPos = [17, 0]  # x, y tuple


def getCharPos(counterX, counterY):
    charPos = (playerPos[0] + counterX, playerPos[1] + counterY)
    return charPos


def checkIfNotInWorld(charPos, worldRows):
    if charPos[0] < 0:
        return True
    elif charPos[1] < 0:
        return True
    elif charPos[0] > len(worldRows[0]) - 1:
        return True
    elif charPos[1] > len(worldRows) - 1:
        return True
    else:
        return False


def buildView(border):
    playerView = """"""
    worldRows = [row for row in world.splitlines() if row]
    counterY = -3
    rows = border.splitlines()
    for i, row in enumerate(rows):
        newRow = ""
        if i == 0 or i == len(rows):
            pass
        elif i == 1 or i == len(rows) - 1:
            newRow = row
            newRow += "\n"
        else:
            counterX = -6
            for j, col in enumerate([char for char in row]):
                if col != '#':
                    newRow += col
                else:
                    charPos = getCharPos(counterX, counterY)
                    if checkIfNotInWorld(charPos, worldRows):
                        newRow += " "
                    else:
                        try:
                            newRow += worldRows[charPos[1]][charPos[0]]
                        except:
                            return (charPos[1], charPos[0])
                    counterX += 1
            newRow += "\n"
        playerView += newRow
        counterY += 1

    temp1 = playerView.splitlines()
    temp2 = [s for s in temp1[2]]
    temp2[7] = "@"
    newtemp = ""
    for i in temp2:
        newtemp += i
    temp2 = newtemp
    temp1[2] = temp2
    thingy = """"""
    for i in temp1:
        thingy += i
        thingy += "\n"
    playerView = thingy
    return playerView


def main(baseScreen):
    mainWindow = curses.newwin(6, 16, 0, 0)
    thingy = buildView(windowBorder)
    mainWindow.addstr(0, 0, thingy)
    mainWindow.refresh()

    while True:
        keyPress = mainWindow.getch()
        if chr(keyPress).lower() == 'w':
            playerPos[1] -= 1
            if playerPos[1] < 0:
                playerPos[1] = 0
            elif playerPos[1] >= maxY:
                playerPos[1] = maxY

        elif chr(keyPress).lower() == 'd':
            playerPos[0] += 1
            if playerPos[0] < 0:
                playerPos[0] = 0
            elif playerPos[0] >= maxX:
                playerPos[0] = maxX

        elif chr(keyPress).lower() == 's':
            playerPos[1] += 1
            if playerPos[1] < 0:
                playerPos[1] = 0
            elif playerPos[1] >= maxY:
                playerPos[1] = maxY

        elif chr(keyPress).lower() == 'a':
            playerPos[0] -= 1
            if playerPos[0] < 0:
                playerPos[0] = 0
            elif playerPos[0] >= maxX:
                playerPos[0] = maxX

        elif chr(keyPress).lower() == 'q':
            return False

        if not isinstance(buildView(windowBorder), str):
            return buildView(windowBorder)
        else:

            mainWindow.addstr(0, 0, buildView(windowBorder))

    curses.napms(5000)


if __name__ == '__main__':
    thingys = curses.wrapper(main)
    print(thingys)
