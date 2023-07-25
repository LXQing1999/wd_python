"""
6.game_clock 
Author:LXQing
Date:2023/7/23
"""
import pygame
pygame.init()
clock=pygame.time.Clock()
i=0
while True:
    clock.tick(1) # 屏幕刷新帧率
    if i<60:
        print(i)
        i+=1
    else:
        break
pygame.quit()
