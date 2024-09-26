import random

from map import *
from settings import *
import pygame
import math
import tkinter as tk
from drawing import mini_map
import tkinter.messagebox as mb
import pygame
from settings import *
from sprite_objects import *
from ray_casting import ray_casting
from drawing import Drawing

inventory = ['фонарик']
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра")

font = pygame.font.Font(None, 24)
r_place = ([1243, 958], [922, 541], [171, 162], [350, 1165])
a = random.randint(0, 100)
if a<=25:
    pedx, pedy= r_place[0]
elif a>25 and a<=50:
    pedx, pedy= r_place[1]
elif a>50 and a<=75:
    pedx, pedy= r_place[2]
elif a>75:
    pedx, pedy= r_place[3]

class Player:
    global text_map1

    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.sensitivity = 0.004

    def show_error(self):
        msg = "вы подняли ключ"
        mb.showinfo("ключик", msg)

    def show_error1(self):
        msg = "Поздравляю, вы прошли игру"
        mb.showinfo("The End", msg)

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        global text_map
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_l]:
            print(pedx,pedy,a)
        if keys[pygame.K_e]:
            print(self.x, self.y)
            if self.x > 1230 and self.x < 1270:
                if self.y > 538 and self.y < 578:
                    if 'ключ' in inventory:
                        self.show_error1()
            if self.x > pedx - 20 and self.x < pedx + 20:
                if self.y > pedy - 20 and self.y < pedy + 20:
                    if not 'ключ' in inventory:
                        print('ключик взят')
                        print(self.x, '   ', self.y)
                        inventory.append('ключ')
                        self.show_error()


        if keys[pygame.K_i]:
            print(inventory)
        if keys[pygame.K_LSHIFT]:
            self.x += 3 * cos_a
            self.y += 3 * sin_a
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02



        self.angle %= DOUBLE_PI

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensitivity
