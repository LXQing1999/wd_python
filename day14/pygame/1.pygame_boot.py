"""
pygame_boot 
Author:LXQing
Date:2023/7/22
"""
import pygame
# 初始化操作
pygame.init()
hero_rectangle=pygame.Rect(100,500,120,125)
print("英雄的原点%d %d"% (hero_rectangle.x,hero_rectangle.y))
print("英雄的尺寸 %d %d"%(hero_rectangle.width,hero_rectangle.height))
# size会返回矩形区域的(宽,高)元组
print("%d %d"% hero_rectangle.size)

# print("游戏代码:")
pygame.quit()