import random
import pygame

from vec2 import Vector
from typing import List
from pygame.locals import K_LEFT, K_RIGHT, KEYDOWN, K_UP, K_DOWN


class Player:
    def __init__(self, x: int, y: int, width: int, height) -> None:
        self.x = x
        self.y = y
        
        self.width = width
        self.height = height

        self.size = 32

        self.speed = Vector(0, 0)

        self.body = [Vector(128, 128)]
        self.food = None

        self.dead = False

    def event(self, event: pygame.event.EventType) -> None:
        if event.type == KEYDOWN:
            if event.key == K_LEFT and self.speed != Vector(self.size, 0):
                self.speed = Vector(-self.size, 0)

            elif event.key == K_RIGHT and self.speed != Vector(-self.size, 0):
                self.speed = Vector(self.size, 0)

            elif event.key == K_UP and self.speed != Vector(0, self.size):
                self.speed = Vector(0, -self.size)

            elif event.key == K_DOWN and self.speed != Vector(0, -self.size):
                self.speed = Vector(0, self.size)

    def update(self) -> None:
        head = self.body[0]

        self.gen_food()

        if head in self.body[1:]:
            self.dead = True

        if head.x < 0 or head.y < 0 or head.x + self.size > self.width or head.y + self.size > self.height:
            self.dead = True

        if self.food == head:
            self.food = None  
            self.body = [head + self.speed] + self.body

        else:
            self.body = [head + self.speed] + self.body[:-1]

    def render(self, screen: pygame.Surface) -> None:

        if self.food:
            pygame.draw.rect(screen, (255, 0, 0), (self.food.x, self.food.y, self.size, self.size))

        for cell in self.body:
            pygame.draw.rect(screen, (255, 255, 255), (cell.x, cell.y, self.size, self.size))

    def gen_food(self):
        if not self.food:
            while True:
                pos = Vector(random.randint(0, self.width // self.size) * self.size, random.randint(0, self.width // self.size) * self.size)

                if pos not in self.body:
                    self.food = pos
                    break
