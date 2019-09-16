import pygame
import pygame.gfxdraw
from pygame.locals import *
import random


pygame.init()

disp_width = 1080
disp_height = 720

disp = pygame.display.set_mode((disp_width, disp_height))
disp.fill((192, 192, 192))
pygame.display.set_caption('Battleboats')

gameState = "welcome"

rects_clicked=[]
rects_missed = []
rects_hit = []
ship_square = [(233, 233, 33, 33), (267, 233, 33, 33 ), (301, 233, 33, 33), (470, 470, 33, 33), (470, 436, 33, 33), (470, 402, 33, 33), (301, 368, 33, 33), (335, 368, 33, 33)]

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
                if isPointInRect(mouseX, mouseY, rects[i][j]) and rects[i][j] in ship_square and not rects[i][j] in rects_clicked:
                    rects_hit.append(rects[i][j])
                    rects_clicked.append(rects[i][j])
                    pygame.draw.rect(disp, (255, 0, 0), rects[i][j])
                    pygame.display.update(rects[i][j])
                    print(rects_clicked)
                elif isPointInRect(mouseX, mouseY, rects[i][j]) and not rects[i][j] in rects_clicked:
                    rects_missed.append(rects[i][j])
                    rects_clicked.append(rects[i][j])
                    pygame.draw.rect(disp, (0, 0, 255), rects[i][j])
                    pygame.display.update(rects[i][j])
                    print(rects_clicked)
        pygame.time.delay(250)

    elif pygame.mouse.get_pressed() != (1, 0, 0):
        newPress = True

if gameState == "welcome":
    l_blue = (80, 171, 250)
    white = (255, 255, 255)
    gameDisplay = pygame.display.set_mode((disp_width,disp_height))
    pygame.display.set_caption('Battleboats')
    clock = pygame.time.Clock()
    gameDisplay.fill(l_blue)
    largeText = pygame.font.Font('freesansbold.ttf',65)
    TextSurf, TextRect = text_objects("Welcome to Battleboats", largeText)
    TextRect.center = ((disp_width/2),(disp_height/4))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
elif gameState == "placeBoats":
    pass
elif gameState == "gamePlay":
    leftGrid = createRects(200, 200)
    rightGrid = createRects(500, 200)

while True:
    event_handler()

    if gameState == "welcome":
        pass
    elif gameState == "placeBoats":
        pass
    elif gameState == "gamePlay":
        trackRects(leftGrid)
