import pygame
from pygame.sprite import Sprite
from random import choice
import os
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game, image):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the alien image and set its rect attribute.
        if(image == None):
            loaded = False
            while not loaded:
                try:
                    path = os.path.join(os.curdir, "images", choice(os.listdir(os.path.join(os.curdir, "images"))))
                    self.image = pygame.image.load(os.path.join(os.curdir, "images", choice(os.listdir(os.path.join(os.curdir, "images")))))
                    os.remove(path)
                    loaded = True
                except FileNotFoundError as e:
                    print(e)
                except:
                    print("OTHER ERROR")
        else:
            self.image = image
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
    def check_edges(self):
    #Return True if alien is at edge of screen.
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    def update(self):
        #Move the alien right or left.
        self.x += (self.settings.alien_speed *
        self.settings.fleet_direction)
        self.rect.x = self.x