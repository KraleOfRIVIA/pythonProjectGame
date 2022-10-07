# Pygame шаблон - скелет для нового проекта Pygame
import sys

import pygame as gay
import random
from pygame.color import THECOLORS
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Создаем игру и окно
gay.init()
gay.mixer.init()
screen = gay.display.set_mode((1200, 800))
screen.fill('white')
font = gay.font.SysFont('couriernew', 40)
text = font.render(str('Gay'), True, 'black')
screen.blit(text, (50, 50))
gay.display.set_caption("My GAY")
clock = gay.time.Clock()
r = gay.Rect(50, 50, 200, 200)
gay.draw.rect(screen,'pink', r, 0)
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(30)
    # Ввод процесса (события)
    for event in gay.event.get():
        screen.blit(text, (500, 50))
        # check for closing window
        if event.type == gay.QUIT:
            gay.quit()
            sys.exit()
    gay.display.flip()