from ast import Pass
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(235, 152, 23)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    pass


def redrawWindow(surface):
    global rows, width
    win.fill((0, 0, 0))
    drawGrid(surface)
    pygame.display.update()


def randomSnack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_Mode((width, height))
    s = snake((235, 153, 23), (10, 10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)
    pass

# rows =
# w =
# h =

# cube.rows = rows
# cube.w = w


main()
