import pygame
import pygame.gfxdraw
from pygame.locals import *
import random


pygame.init()

disp_width = 1080
disp_height = 720

disp = pygame.display.set_mode((disp_width, disp_height))
disp.fill((255, 255, 255))
pygame.display.set_caption('Battleship')


def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or ( event.type == KEYDOWN and ( event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            quit()

def createRects(x, y):
    """Creates an 8x8 grid of squares
    
    Keyword Arguments:
    x -- the x position for the top right corner of the grid to start at
    y -- the y position for the top right corner of the grid to start at
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

while True:
    event_handler()
    createRects(200, 200)
    createRects(500, 200)

    pygame.display.update()