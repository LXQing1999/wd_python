"""
5.print_hero 
Author:LXQing
Date:2023/7/23
"""
import pygame.image

pygame.init()
screen = pygame.display.set_mode((480, 700))
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()
pygame.quit()
