import pygame 
from data import *

pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], seting_win["HEIGHT"]))
pygame.display.set_caption("Ping Pong")

def run():
    game = True 

    boart = pygame.Rect(15,
                        seting_win["HEIGHT"] // 2 - setting_boar)

    while game:
        window.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False




run()



