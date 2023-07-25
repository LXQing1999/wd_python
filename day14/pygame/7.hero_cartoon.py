"""
hero_cartoon 
Author:LXQing
Date:2023/7/23
"""
import pygame
pygame.init()
screen=pygame.display.set_mode((480,700))
# load背景图
bg=pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))
pygame.display.update()
clock=pygame.time.Clock()
# 定义rect记录飞机的初始位置
hero_rect=pygame.Rect(150,300,102,126)

while True:
    # 指定循环体内部代码执行的频率
    clock.tick(60)
    # 修改飞机的位置
    hero_rect.y-=1
    if hero_rect.y<0:
        hero_rect.y=700
    # 调用blit方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    # 调用updata方法更新显示
    pygame.display.update()
