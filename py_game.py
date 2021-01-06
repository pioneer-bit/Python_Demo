# Author:丁泽盛
# data:2020/10/5 13:00

import sys
import pygame

def run_game():

    pygame.init()  #初始化游戏背景设置
    screen = pygame.display.set_mode((900, 600))#创建显示窗口
    pygame.display.set_caption('Alien Invasion')
    bg_color = (230, 9, 0)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()

run_game()
