import websocket_interface
import websockets
import asyncio
import pygame

def messageRecieve():
    pass

def messageSend():
    pass

def connectToServer(ip_to_try):
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption('Limited Vision Shooter')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((30, 30, 30))
    
    font = pygame.font.Font(None, 36)
