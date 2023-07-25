"""
4.background 显示背景图
Author:LXQing
Date:2023/7/23
"""
import pygame.image
pygame.init()
screen = pygame.display.set_mode((480, 700))
bg=pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
pygame.display.update()
while True:
    pass
pygame.quit()