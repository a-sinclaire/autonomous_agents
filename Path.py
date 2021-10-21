import pygame.draw
import numpy as np


class Path:
    def __init__(self, surface, start, end, r=20):
        self.surface = surface
        self.start = start
        self.end = end
        self.radius = r

        self.color = (255, 255, 255)

    def draw(self, draw_radius=False):
        if draw_radius:
            pygame.draw.line(self.surface, (100, 100, 100), (self.start.x, self.start.y), (self.end.x, self.end.y), self.radius*2)
        pygame.draw.line(self.surface, self.color, (self.start.x, self.start.y), (self.end.x, self.end.y))
