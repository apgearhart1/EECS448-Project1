import pygame
import pygame.gfxdraw
from pygame.locals import *
from boats import Boat
from executive import Executive

pygame.init()

disp_width = 1080
disp_height = 720

disp = pygame.display.set_mode((disp_width, disp_height))
disp.fill((192, 192, 192))
pygame.display.set_caption('Battleboats')
clock = pygame.time.Clock()
draw_once=True
gameState = "welcome"

numberOfBoats = 4

numberOfBoats = 0

placeNumber = 1
spotsToCheck = [] #[[0 for x in range(2)] for y in range(placeNumber)]

grid = None
leftGrid = None
rightGrid = None

# vaiables used when gameState = "gamePlay"
checkbox=pygame.draw.rect(disp, (255, 255, 255), (533, 200, 15, 15))
toggled=False

rects_clicked1=[]
rects_missed1 = []
rects_hit1 = []
opposing_ship1 = [(0,0), (0,1), (0,2), (0,3), (4,4), (3,4), (7,7), (7,6), (7,5)]
my_ships1 = [(1,1), (2,1), (3,1), (4,1), (7,7), (6,7), (4,3), (4,4), (4,5)]

rects_clicked2=[]
rects_missed2 = []
rects_hit2 = []
opposing_ship2 = my_ships1
my_ships2 = opposing_ship1
#game = Executive()

board_cleared=True

def quitGame():
    pygame.quit()
    quit()

def event_handler():
    """Checks for different pygame events"""

    for event in pygame.event.get():
        if event.type == QUIT or ( event.type == KEYDOWN and ( event.key == K_ESCAPE or event.key == K_q)):
            quitGame()

def isPointInRect(x, y, rect):
    """Checks if a coordinate is within the bounds of a pygame.rect object

    Args:
    x (float): x coordinate to check
    y (float): y coordinate to check
    rect (pygame.Rect): object to see if x any y are in

    Returns:
        bool: True if x and y are in rect, False otherwise
    """

    if x < rect.x + rect.width and x > rect.x and y < rect.y + rect.height and y > rect.y:
        return True
    return False

def createRects(x, y):
    """Creates an 8x8 grid of squares

    Args:
    x (int): the x position for the top right corner of the grid to start at
    y (int): the y position for the top right corner of the grid to start at

    Returns:
        8x8 array of pygame.Rect objects
    """

    interval = (disp_width / 2) / 16
    divX = interval + x
    divY = interval + y
    rects = [[0 for x in range(8)] for y in range(8)]
    for i in range(0, 8):
        for j in range(0, 8):
            rects[i][j] = pygame.Rect(divX, divY, interval, interval)
            pygame.draw.rect(disp, (0, 0, 0), rects[i][j], 2)
            divX += interval
        divX = interval + x
        divY += interval

    pygame.display.update()
    return rects

def text_objects(text, font): #function used from https://pythonprogramming.net/pygame-start-menu-tutorial/
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()

def showboat1(rects):
    for i in range(0, 8):
        for j in range(0, 8):
            if(i,j) in my_ships1:
                pygame.draw.rect(disp, (0, 0, 0), rects[i][j])
                pygame.display.update(rects[i][j])

def showboat2(rects):
    for i in range(0, 8):
        for j in range(0, 8):
            if(i,j) in my_ships2:
                pygame.draw.rect(disp, (0, 0, 0), rects[i][j])
                pygame.display.update(rects[i][j])



def trackRects1(rects):
    """Tracks when a single square in a grid is pressed by the mouse for player 1

    Args:
        rects (8x8 array of pygame.Rect objects): the grid to check on
    """

    newPress = True
    mouseX = 0
    mouseY = 0

    if pygame.mouse.get_pressed() == (1, 0, 0) and newPress:
        newPress = False
        mouseX, mouseY = pygame.mouse.get_pos()
        for i in range(0, 8):
            for j in range(0, 8):
                if isPointInRect(mouseX, mouseY, rects[i][j]) and (i,j) in opposing_ship1 and not (i,j) in rects_clicked1: #clicked on square containing ship
                    rects_hit1.append((i,j))
                    rects_clicked1.append((i,j))
                    pygame.draw.rect(disp, (255, 0, 0), rects[i][j])
                    pygame.display.update(rects[i][j])
                    print(rects_clicked1)
                elif isPointInRect(mouseX, mouseY, rects[i][j]) and not (i,j) in rects_clicked1: #clicked on a square and missed
                    rects_missed1.append((i,j))
                    rects_clicked1.append((i,j))
                    pygame.draw.rect(disp, (0, 0, 255), rects[i][j])
                    pygame.display.update(rects[i][j])
                    print(rects_clicked1)
                    pygame.time.delay(250)
                    setupGamePlay2()



def trackRects2(rects):
    """Tracks when a single square in a grid is pressed by the mouse for player 2

    Args:
        rects (8x8 array of pygame.Rect objects): the grid to check on
    """

    newPress = True
    mouseX = 0
    mouseY = 0


    if pygame.mouse.get_pressed() == (1, 0, 0) and newPress:
        newPress = False
        mouseX, mouseY = pygame.mouse.get_pos()
        for i in range(0, 8):
            for j in range(0, 8):
                if isPointInRect(mouseX, mouseY, rects[i][j]) and (i,j) in opposing_ship2 and not (i,j) in rects_clicked2:
                    rects_hit2.append((i,j))
                    rects_clicked2.append((i,j))
                    pygame.draw.rect(disp, (255, 0, 0), rects[i][j])
                    pygame.display.update(rects[i][j])
                    print(rects_clicked2)
                elif isPointInRect(mouseX, mouseY, rects[i][j]) and not (i,j) in rects_clicked2:
                    rects_missed2.append((i,j))
                    rects_clicked2.append((i,j))
                    pygame.draw.rect(disp, (0, 0, 255), rects[i][j])
                    pygame.display.update(rects[i][j])
                    print(rects_clicked2)
                    pygame.time.delay(250)
                    setupGamePlay1()


    elif pygame.mouse.get_pressed() != (1, 0, 0):
        newPress = True

def printRects1(rects):
    for i in range(0,8):
        for j in range(0,8):
            if (i,j) in rects_hit1:
                pygame.draw.rect(disp, (255, 0, 0), rects[i][j])
                pygame.display.update(rects[i][j])
            if (i, j) in rects_missed1:
                pygame.draw.rect(disp, (0, 0, 255), rects[i][j])
                pygame.display.update(rects[i][j])

def printRects2(rects):
    for i in range(0,8):
        for j in range(0,8):
            if (i,j) in rects_hit2:
                pygame.draw.rect(disp, (255, 0, 0), rects[i][j])
                pygame.display.update(rects[i][j])
            if (i, j) in rects_missed2:
                pygame.draw.rect(disp, (0, 0, 255), rects[i][j])
                pygame.display.update(rects[i][j])


def track_toggle() :
    global toggled
    newPress = True
    mouseX = 0
    mouseY = 0


    if pygame.mouse.get_pressed() == (1, 0, 0) and newPress:
        newPress = False
        mouseX, mouseY = pygame.mouse.get_pos()
        if isPointInRect(mouseX, mouseY, pygame.Rect(533, 200, 15, 15)):
            if not toggled:
                checkbox=pygame.draw.rect(disp, (0, 0, 0), (533, 200, 15, 15))
                pygame.display.update(pygame.Rect(533, 200, 15, 15))
                toggled=True
            else:
                checkbox=pygame.draw.rect(disp, (255, 255, 255), (533, 200, 15, 15))
                pygame.display.update(pygame.Rect(533, 200, 15, 15))
                toggled=False

    elif pygame.mouse.get_pressed() != (1, 0, 0):
        newPress = True

def clear_board(rects):
    for i in range(0, 8):
        for j in range(0, 8):
            pygame.draw.rect(disp, (192, 192, 192), rects[i][j])
            pygame.display.update(rects[i][j])

def trackPlacement(rects):
    """ tracks the placement of boats on the placeBoats screens for player 1 and 2

    Args:
        rects (8x8 array of pygame.Rect objects): grid to check on
    """

    global placeNumber
    global spotsToCheck

    newPress = True
    mouseX = 0
    mouseY = 0

    if pygame.mouse.get_pressed() == (1, 0, 0) and newPress:
        newPress = False
        mouseX, mouseY = pygame.mouse.get_pos()
        for i in range(0, 8):
            for j in range(0, 8):
                if isPointInRect(mouseX, mouseY, rects[i][j]) and [i, j] not in spotsToCheck and len(spotsToCheck) < placeNumber:
                    spotsToCheck.append([i, j])
                    pygame.draw.rect(disp, (0, 0, 0), rects[i][j])
                    pygame.display.update(rects[i][j])

    elif pygame.mouse.get_pressed() != (1, 0, 0) and len(spotsToCheck) == placeNumber:
        newPress = True
        print("spotsToCheck:", spotsToCheck)
        B = Boat()
        if B.validPlace(spotsToCheck):
            print("Boat Placed")
            placeNumber += 1
            updateBoatToPlaceText(placeNumber)
            if gameState == "placeBoats1":
                #TODO add this boat to player1's list of boat placements
                pass
            elif gameState == "placeBoats2":
                #TODO add this boat to player2's list of boat placements
                pass
        else:
            print("Error placing boat")
            for i in spotsToCheck:
                pygame.draw.rect(disp, (192, 192, 192), rects[i[0]][i[1]])
                pygame.draw.rect(disp, (0, 0, 0), rects[i[0]][i[1]], 2)
                pygame.display.update(rects[i[0]][i[1]])
        spotsToCheck = []
    elif len(spotsToCheck) != placeNumber:
        print("Boat not long enough")
        for i in spotsToCheck:
            pygame.draw.rect(disp, (192, 192, 192), rects[i[0]][i[1]])
            pygame.draw.rect(disp, (0, 0, 0), rects[i[0]][i[1]], 2)
            pygame.display.update(rects[i[0]][i[1]])
        spotsToCheck = []

def trackPlayButton():
    """ Tracks if the Play button on the welcome screen has been pressed. If it has, setupPlaceBoats(1) is called"""

    global gameState

    if pygame.mouse.get_pressed() == (1, 0, 0):
        mouseX, mouseY = pygame.mouse.get_pos()
        if isPointInRect(mouseX, mouseY, pygame.Rect(disp_width*.45,disp_height*.43,120,75)) and not numberOfBoats==0:
            setupPlaceBoats(1)


def getSize():
    """Handles the user interface of selecting the size of the boats

    Args:
    None
    Returns:
    size - Number of boats
    """
    global draw_once
    global numberOfBoats
    white = (255, 255, 255)
    black = (0,0,0)
    green = (0, 255, 0)

    if draw_once==True:
        pygame.draw.rect(disp, black ,(disp_width*.33 ,disp_height*.30, 70,70))
        pygame.draw.rect(disp, black ,(disp_width*.33 + 85,disp_height*.30, 70,70))
        pygame.draw.rect(disp, black ,(disp_width*.33 + 170,disp_height*.30, 70,70))
        pygame.draw.rect(disp, black ,(disp_width*.33 + 255,disp_height*.30, 70,70))
        pygame.draw.rect(disp, black ,(disp_width*.33 + 340,disp_height*.30, 70,70))
        pygame.display.update()
        draw_once=False
    largeText = pygame.font.Font('freesansbold.ttf',65)
    blackText = pygame.font.Font('freesansbold.ttf',65)
    medText = pygame.font.Font('freesansbold.ttf', 48)
    smallText = pygame.font.Font('freesansbold.ttf', 36)
    TextSurf, TextRect = text_objects("1", largeText)
    TextSurf2, TextRect2 = text_objects("2", largeText)
    TextSurf3, TextRect3 = text_objects("3", largeText)
    TextSurf4, TextRect4 = text_objects("4", largeText)
    TextSurf5, TextRect5 = text_objects("5", largeText)
    TextRect.center = ((disp_width*.36),(disp_height*.35))
    TextRect2.center = ((disp_width*.36 + 85),(disp_height*.35))
    TextRect3.center = ((disp_width*.36 + 170), (disp_height*.35))
    TextRect4.center = ((disp_width*.36 + 255), (disp_height*.35))
    TextRect5.center = ((disp_width*.36 + 340), (disp_height*.35))
    disp.blit(TextSurf, TextRect)
    disp.blit(TextSurf2, TextRect2)
    disp.blit(TextSurf3, TextRect3)
    disp.blit(TextSurf4, TextRect4)
    disp.blit(TextSurf5, TextRect5)

    if pygame.mouse.get_pressed() == (1, 0, 0):
        mouseX, mouseY = pygame.mouse.get_pos()
        if isPointInRect(mouseX, mouseY, pygame.Rect(disp_width*.33,disp_height*.30,70,70)):
            numberOfBoats = 1
            pygame.draw.rect(disp, green ,(disp_width*.33 ,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 85,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 170,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 255,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 340,disp_height*.30, 70,70))
            TextSurf, TextRect = text_objects("1", largeText)
            TextSurf2, TextRect2 = text_objects("2", largeText)
            TextSurf3, TextRect3 = text_objects("3", largeText)
            TextSurf4, TextRect4 = text_objects("4", largeText)
            TextSurf5, TextRect5 = text_objects("5", largeText)
            pygame.display.update()
        elif isPointInRect(mouseX, mouseY, pygame.Rect(disp_width*.33+85,disp_height*.30,70,70)):
            numberOfBoats = 2
            pygame.draw.rect(disp, black ,(disp_width*.33 ,disp_height*.30, 70,70))
            pygame.draw.rect(disp, green ,(disp_width*.33 + 85,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 170,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 255,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 340,disp_height*.30, 70,70))
            TextSurf, TextRect = text_objects("1", largeText)
            TextSurf2, TextRect2 = text_objects("2", largeText)
            TextSurf3, TextRect3 = text_objects("3", largeText)
            TextSurf4, TextRect4 = text_objects("4", largeText)
            TextSurf5, TextRect5 = text_objects("5", largeText)
            pygame.display.update()
        elif isPointInRect(mouseX, mouseY, pygame.Rect(disp_width*.33+170,disp_height*.30,70,70)):
            numberOfBoats = 3
            pygame.draw.rect(disp, black ,(disp_width*.33 ,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 85,disp_height*.30, 70,70))
            pygame.draw.rect(disp, green ,(disp_width*.33 + 170,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 255,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 340,disp_height*.30, 70,70))
            TextSurf, TextRect = text_objects("1", largeText)
            TextSurf2, TextRect2 = text_objects("2", largeText)
            TextSurf3, TextRect3 = text_objects("3", largeText)
            TextSurf4, TextRect4 = text_objects("4", largeText)
            TextSurf5, TextRect5 = text_objects("5", largeText)
            pygame.display.update()
        elif isPointInRect(mouseX, mouseY, pygame.Rect(disp_width*.33+255,disp_height*.30,70,70)):
            numberOfBoats = 4
            pygame.draw.rect(disp, black ,(disp_width*.33 ,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 85,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 170,disp_height*.30, 70,70))
            pygame.draw.rect(disp, green ,(disp_width*.33 + 255,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 340,disp_height*.30, 70,70))
            TextSurf, TextRect = text_objects("1", largeText)
            TextSurf2, TextRect2 = text_objects("2", largeText)
            TextSurf3, TextRect3 = text_objects("3", largeText)
            TextSurf4, TextRect4 = text_objects("4", largeText)
            TextSurf5, TextRect5 = text_objects("5", largeText)
            pygame.display.update()
        elif isPointInRect(mouseX, mouseY, pygame.Rect(disp_width*.33+340,disp_height*.30,70,70)):
            numberOfBoats = 5
            pygame.draw.rect(disp, black ,(disp_width*.33 ,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 85,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 170,disp_height*.30, 70,70))
            pygame.draw.rect(disp, black ,(disp_width*.33 + 255,disp_height*.30, 70,70))
            pygame.draw.rect(disp, green ,(disp_width*.33 + 340,disp_height*.30, 70,70))
            TextSurf, TextRect = text_objects("1", largeText)
            TextSurf2, TextRect2 = text_objects("2", largeText)
            TextSurf3, TextRect3 = text_objects("3", largeText)
            TextSurf4, TextRect4 = text_objects("4", largeText)
            TextSurf5, TextRect5 = text_objects("5", largeText)
            pygame.display.update()

    pygame.display.update()


def trackQuitButton():
    """ Tracks if the Quit button on the welcome screen has been pressed. If it has, quitGame() is called"""

    if pygame.mouse.get_pressed() == (1, 0, 0):
        mouseX, mouseY = pygame.mouse.get_pos()
        if isPointInRect(mouseX, mouseY, pygame.Rect(disp_width*.45,disp_height*.68,120,75)):
            quitGame()

def updateBoatToPlaceText(size):
    """ Every time this is called, the text that says "Boat size to place..." on gameState = "placeBoats1"
        or gameState = "placeBoats2" will get redrawn with the new size shown

    Args:
        size (int): should corresponds to size of current boat to place (e.g. global placeNumber)
    """

    disp.fill((192, 192, 192), (350, 135, 200, 40))
    pygame.display.update((350, 135, 200, 40))
    font = pygame.font.SysFont("Times New Roman", 30)
    text = font.render("Boat size to place: " + str(size), True, (0, 128, 0))
    disp.blit(text, (350, 135))
    pygame.display.update((350, 135, 200, 40))

def showSwitchPlayers(originalTime):
    """ Displays the screen that tells players to switch. Gives players three seconds to do so.

    Args:
        originalTime (pygame.time.get_ticks()): represents the original time (in systicks, represented as int)
                                                that this method was called. It is used agains the current
                                                time in systics to see if three seconds has passed
    """

    global placeNumber
    global gameState

    disp.fill((192, 192, 192))
    font = pygame.font.SysFont("Times New Roman", 40)
    text = font.render("Switch Players", True, (0, 128, 0))
    disp.blit(text, (350, 100))
    pygame.display.update()
    while pygame.time.get_ticks() < originalTime + 3000:
        event_handler()

    setupPlaceBoats(2)

def setupWelcome():
    """ Sets up initial graphics and variables for the welcome state """

    l_blue = (80, 171, 250)
    white = (255, 255, 255)
    black = (0,0,0)
    pygame.display.set_caption('Battleboats')
    disp.fill(l_blue)
    largeText = pygame.font.Font('freesansbold.ttf',65)
    TextSurf, TextRect = text_objects("Welcome to Battleboats", largeText)
    medText = pygame.font.Font('freesansbold.ttf', 48)
    smallText = pygame.font.Font('freesansbold.ttf', 36)
    TextSurf, TextRect = text_objects("Welcome to Battleboats", largeText)
    TextSurf2, TextRect2 = text_objects("Play", medText)
    TextSurf3, TextRect3 = text_objects("Quit", medText)
    TextRect.center = ((disp_width/2),(disp_height*.15))
    TextRect2.center = ((disp_width/2), (disp_height/2))
    TextRect3.center = ((disp_width/2), (disp_height*.75))
    #makes buttons interactive
    mouse = pygame.mouse.get_pos()
    if disp_width*.45 + 100 > mouse[0] > disp_width*.45 and disp_height*.43 + 50 > mouse[1] > disp_height*.43:
        pygame.draw.rect(disp, white ,(disp_width*.45,disp_height*.43,120,75))
    elif disp_width*.45 + 100 > mouse[0] > disp_width*.45 and disp_height*.68 + 50 > mouse[1] > disp_height*.68:
        pygame.draw.rect(disp, white ,(disp_width*.45,disp_height*.68,120,75))
    else:
        pygame.draw.rect(disp, l_blue ,(disp_width*.45,disp_height*.43,120,75))
        pygame.draw.rect(disp, l_blue ,(disp_width*.45,disp_height*.68,120,75))
        pygame.draw.rect(disp, black,(disp_width*.45,disp_height*.43,120,75),5)
        pygame.draw.rect(disp, black,(disp_width*.45,disp_height*.68,120,75),5)
    TextRect.center = ((disp_width/2),(disp_height/4))
    disp.blit(TextSurf, TextRect)
    disp.blit(TextSurf2, TextRect2)
    disp.blit(TextSurf3, TextRect3)
    pygame.display.update()

def setupPlaceBoats(whichPlayer):
    """ Sets up initial graphics and variables for the placeBoats state

    Args:
        whichPlayer (int): 1 -> setup the placeBoats state for player 1, 2 -> setup the placeBoates satate for player 2
    """

    global gameState
    global grid
    global placeNumber
    global spotsToCheck

    placeNumber = 1
    spotsToCheck = []

    disp.fill((192, 192, 192))
    font = pygame.font.SysFont("Times New Roman", 40)
    text = font.render("Player " + str(whichPlayer) + ": " + "Place your " + str(numberOfBoats) + " boats", True, (0, 128, 0))
    disp.blit(text, (350, 100))

    updateBoatToPlaceText(1)

    grid = createRects(350, 200)

    pygame.display.update()
    gameState = "placeBoats" + str(whichPlayer)


def setupGamePlay1():
    """ Sets up initial graphics and variables for the gamePlay state """

    global leftGrid
    global rightGrid
    global gameState

    disp_width = 1080
    disp_height = 720
    disp = pygame.display.set_mode((disp_width, disp_height))
    disp.fill((192, 192, 192))
    pygame.display.set_caption('Battleboats')
    player_turn=pygame.font.SysFont('Consolas', 40)
    player_turn_display=player_turn.render("PLAYER 1's TURN", False, (0, 0, 0))
    toggle = pygame.font.SysFont('Ariel', 20)
    toggle_display=toggle.render('  SHOW MY BOATS', False, (0, 0, 0))
    checkbox=pygame.draw.rect(disp, (255, 255, 255), (533, 200, 15, 15))
    toggled=False
    board_cleared=True
    track_toggle()
    disp.blit(player_turn_display, (350, 0))
    disp.blit(toggle_display, (548,200))
    leftGrid = createRects(200, 200)
    rightGrid = createRects(500, 200)
    gameState = "gamePlay1"

def setupGamePlay2():
    """ Sets up initial graphics and variables for the gamePlay state """

    global leftGrid
    global rightGrid
    global gameState

    disp_width = 1080
    disp_height = 720
    disp = pygame.display.set_mode((disp_width, disp_height))
    disp.fill((192, 192, 192))
    pygame.display.set_caption('Battleboats')
    player_turn=pygame.font.SysFont('Consolas', 40)
    player_turn_display=player_turn.render("PLAYER 2's TURN", False, (0, 0, 0))
    toggle = pygame.font.SysFont('Ariel', 20)
    toggle_display=toggle.render('  SHOW MY BOATS', False, (0, 0, 0))
    checkbox=pygame.draw.rect(disp, (255, 255, 255), (533, 200, 15, 15))
    toggled=False
    board_cleared=True
    track_toggle()
    disp.blit(player_turn_display, (350, 0))
    disp.blit(toggle_display, (548,200))
    leftGrid = createRects(200, 200)
    rightGrid = createRects(500, 200)
    gameState = "gamePlay2"


setupWelcome()

while True:
    event_handler()
    if gameState == "welcome":
        trackPlayButton()
        getSize()
        if numberOfBoats <= 5 and numberOfBoats > 0:
            trackPlayButton()
        trackQuitButton()

    elif gameState == "placeBoats1":
        if placeNumber <= numberOfBoats:
            trackPlacement(grid)
        else:
            gameState = "None"
            showSwitchPlayers(pygame.time.get_ticks())

    elif gameState == "placeBoats2":
        if placeNumber <= numberOfBoats:
            trackPlacement(grid)
        else:
            gameState = "None"
            setupGamePlay1()

    elif gameState == "gamePlay1":
        printRects1(leftGrid)
        printRects2(rightGrid)
        trackRects1(leftGrid)
        track_toggle()
        if toggled and board_cleared:
            showboat1(rightGrid)
            board_cleared=False
        if not toggled and not board_cleared:
            clear_board(rightGrid)
            rightGrid=createRects(500, 200)
            board_cleared=True
    elif gameState == "gamePlay2":
        printRects2(leftGrid)
        printRects1(rightGrid)
        trackRects2(leftGrid)
        track_toggle()
        if toggled and board_cleared:
            showboat2(rightGrid)
            board_cleared=False
        if not toggled and not board_cleared:
            clear_board(rightGrid)
            rightGrid=createRects(500, 200)
            board_cleared=True
    clock.tick(30)
