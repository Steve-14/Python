import sys
import pygame
from settings import Settings

class AlienInvasion:
    #Overall class to manage game assets and behaviour.
    
    def __init__(self):
        #iNITIALISE THE GAME and create game resources.
        pygame.init()

self.screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Alien Invasion")

# set background colour
self.bg_color = (230, 230, 230)

def run_game(self):
    #"""Start main loop for the game"""
    while True:
        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # Redraw the screen for each pass thru the loop.
        self.screen.fill(self.bg_color)
                
        #nake most recent screen visable
        pygame.display.flip()
                
if __name__ == "__main__":
    # make  a game instance and run
    ai = AlienInvasion()
    ai.run_game