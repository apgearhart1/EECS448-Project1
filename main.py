import pygame
from pygame.locals import *


pygame.init()

disp_width = 1080
disp_height = 720

disp = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption('Battleship')


def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (
             event.type == KEYDOWN and (
              event.key == K_ESCAPE or
              event.key == K_q
             )):
            pygame.quit()
            quit()

while True:
    event_handler()
    pygame.draw.circle(disp, (0,0,255), (150, 50), 30, 1)
    pygame.display.update()