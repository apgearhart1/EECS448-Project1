import pygame
import pygame.gfxdraw
from pygame.locals import *
from boats import Boat

pygame.init()

disp_width = 1080
disp_height = 720

disp = pygame.display.set_mode((disp_width, disp_height))
disp.fill((192, 192, 192))
pygame.display.set_caption('Battleboats')
clock = pygame.time.Clock()

gameState = "placeBoats1"
numberOfBoats = 4
placeNumber = 1
spotsToCheck = [] #[[0 for x in range(2)] for y in range(placeNumber)]

grid = None
leftGrid = None
rightGrid = None

def event_handler():
    """Checks for different pygame events"""

    for event in pygame.event.get():
        if event.type == QUIT or ( event.type == KEYDOWN and ( event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            quit()

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
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def showboat(rects):
    for i in range(0, 8):
        for j in range(0, 8):
            if(i,j) in my_ships:
                pygame.draw.rect(disp, (0, 0, 0), rects[i][j])
                pygame.display.update(rects[i][j])



def trackRects(rects):
    """Tracks when a single square in a grid is pressed by the mouse

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
                if isPointInRect(mouseX, mouseY, rects[i][j]) and (i,j) in ship_square and not (i,j) in rects_clicked:
                    rects_hit.append((i,j))
                    rects_clicked.append((i,j))
                    pygame.draw.rect(disp, (255, 0, 0), rects[i][j])
                    pygame.display.update(rects[i][j])
                    print(rects_clicked)
                elif isPointInRect(mouseX, mouseY, rects[i][j]) and not (i,j) in rects_clicked:
                    rects_missed.append((i,j))
                    rects_clicked.append((i,j))
                    pygame.draw.rect(disp, (0, 0, 255), rects[i][j])
                    pygame.display.update(rects[i][j])
                    print(rects_clicked)

        pygame.time.delay(250)

    elif pygame.mouse.get_pressed() != (1, 0, 0):
        newPress = True

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
                if isPointInRect(mouseX, mouseY, rects[i][j]) and [j, i] not in spotsToCheck and len(spotsToCheck) < placeNumber:
                    spotsToCheck.append([j, i])
                    pygame.draw.rect(disp, (0, 0, 0), rects[i][j])
                    pygame.display.update(rects[i][j])

    elif pygame.mouse.get_pressed() != (1, 0, 0) and len(spotsToCheck) != 0:
        newPress = True
        print(spotsToCheck)
        B = Boat()
        if B.validPlace(spotsToCheck):
            print("Boat Placed")
            placeNumber += 1
            disp.fill((192, 192, 192), (350, 135, 200, 40))
        else:
            print("Error placing boat")
            for i in spotsToCheck:
                pygame.draw.rect(disp, (192, 192, 192), rects[i[1]][i[0]])
                pygame.draw.rect(disp, (0, 0, 0), rects[i[1]][i[0]], 2)
                pygame.display.update(rects[i[1]][i[0]])

        spotsToCheck = []

if gameState == "welcome":
    l_blue = (80, 171, 250)
    white = (255, 255, 255)
    black = (0,0,0)
    gameDisplay = pygame.display.set_mode((disp_width,disp_height))
    pygame.display.set_caption('Battleboats')
    gameDisplay.fill(l_blue)
    largeText = pygame.font.Font('freesansbold.ttf',65)
    TextSurf, TextRect = text_objects("Welcome to Battleboats", largeText)
    medText = pygame.font.Font('freesansbold.ttf', 48)
    smallText = pygame.font.Font('freesansbold.ttf', 36)
    TextSurf, TextRect = text_objects("Welcome to Battleboats", largeText)
    TextSurf2, TextRect2 = text_objects("Play", medText)
    TextSurf3, TextRect3 = text_objects("Quit", medText)
    TextRect.center = ((disp_width/2),(disp_height/4))
    TextRect2.center = ((disp_width/2), (disp_height/2))
    TextRect3.center = ((disp_width/2), (disp_height*.75))
    #makes buttons interactive
    mouse = pygame.mouse.get_pos()
    if disp_width*.45 + 100 > mouse[0] > disp_width*.45 and disp_height*.43 + 50 > mouse[1] > disp_height*.43:
        pygame.draw.rect(gameDisplay, white ,(disp_width*.45,disp_height*.43,120,75))
    elif disp_width*.45 + 100 > mouse[0] > disp_width*.45 and disp_height*.68 + 50 > mouse[1] > disp_height*.68:
        pygame.draw.rect(gameDisplay, white ,(disp_width*.45,disp_height*.68,120,75))
    else:
        pygame.draw.rect(gameDisplay, l_blue ,(disp_width*.45,disp_height*.43,120,75))
        pygame.draw.rect(gameDisplay, l_blue ,(disp_width*.45,disp_height*.68,120,75))
        pygame.draw.rect(gameDisplay, black,(disp_width*.45,disp_height*.43,120,75),5)
        pygame.draw.rect(gameDisplay, black,(disp_width*.45,disp_height*.68,120,75),5)
    TextRect.center = ((disp_width/2),(disp_height/4))
    gameDisplay.blit(TextSurf, TextRect)
    gameDisplay.blit(TextSurf2, TextRect2)
    gameDisplay.blit(TextSurf3, TextRect3)
    pygame.display.update()

elif gameState == "placeBoats1":
    font = pygame.font.SysFont("Times New Roman", 40)
    text = font.render("Player 1, Place your " + str(numberOfBoats) + " boats", True, (0, 128, 0))
    disp.blit(text, (350, 100))

    grid = createRects(350, 200)

    pygame.display.update()

elif gameState == "gamePlay":
    disp_width = 1080
    disp_height = 720
    disp = pygame.display.set_mode((disp_width, disp_height))
    disp.fill((192, 192, 192))
    pygame.display.set_caption('Battleboats')
    toggle = pygame.font.SysFont('Ariel', 20)
    toggle_display=toggle.render('  SHOW MY SHIPS', False, (0, 0, 0)) #☑
    disp.blit(toggle_display, (548,200))
    checkbox=pygame.draw.rect(disp, (255, 255, 255), (533, 200, 15, 15))
    toggled=False
    rects_clicked=[]
    rects_missed = []
    rects_hit = []
    ship_square = [(0,0), (0,1), (0,2), (0,3), (4,4), (3,4), (7,7), (7,6), (7,5)]
    my_ships = [(1,1), (2,1), (3,1), (4,1), (7,7), (6,7), (4,3), (4,4), (4,5)]
    leftGrid = createRects(200, 200)
    rightGrid = createRects(500, 200)
    board_cleared=True


while True:
    event_handler()
    if gameState == "welcome":
        pass

    elif gameState == "placeBoats1":
        if placeNumber <= numberOfBoats:
            font = pygame.font.SysFont("Times New Roman", 30)
            text = font.render("Boat to place: " + str(placeNumber) + "x" + str(placeNumber), True, (0, 128, 0))
            disp.blit(text, (350, 135))
            trackPlacement(grid)
            pygame.display.update((350, 135, 200, 40))
        else:
            pass
            #go to next screen

    elif gameState == "gamePlay":
        trackRects(leftGrid)
        track_toggle()
        if toggled and board_cleared:
            showboat(rightGrid)
            board_cleared=False
        if not toggled and not board_cleared:
            clear_board(rightGrid)
            rightGrid=createRects(500, 200)
            board_cleared=True
    clock.tick(30)