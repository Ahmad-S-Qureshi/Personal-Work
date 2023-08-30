import pygame
from pygame.locals import *
class text_drawer:
    def __init__(self):
        pass

    # Draws centered text
    def drawCenteredText(self, text, background, font, height, screen):

        # Renders text onto a pygame rect object at the height of the input
        tempText = font.render(text, 1, (180, 180, 180))
        tempTextRect = tempText.get_rect()
        tempTextPos = Rect(0, height, tempTextRect.w, tempTextRect.h)

        # Grabs the center X-value of the screen
        centerXPos = background.get_rect().centerx
        tempTextPos.centerx = centerXPos
        background.blit(tempText, tempTextPos)