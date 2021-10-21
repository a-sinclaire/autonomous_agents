import numpy as np
import random


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def static_add(v1, v2):
        return Vector(v1.x+v2.x, v1.y+v2.y)

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y
        return self

    @staticmethod
    def static_sub(v1, v2):
        return Vector(v1.x-v2.x, v1.y-v2.y)

    def sub(self, v):
        new_v = Vector.static_sub(self, v)
        self.set(new_v.x, new_v.y)
        return self

    def set(self, x, y):
        self.x = x
        self.y = y
        return self

    def get_heading(self):
        return np.arctan2(self.y, self.x)

    def normalize(self):
        self.set_mag(1)
        return self

    def get_mag(self):
        return np.sqrt(np.power(self.x, 2) + np.power(self.y, 2))

    def set_mag(self, new_mag):
        mag = self.get_mag()
        if mag == 0:
            return self
        new_x = self.x * new_mag / mag
        new_y = self.y * new_mag / mag
        self.set(new_x, new_y)
        return self

    def limit(self, limit):
        if self.get_mag() > limit:
            self.set_mag(limit)
        return self

    def mult(self, m):
        self.x *= m
        self.y *= m
        return self

    def copy(self):
        return Vector(self.x, self.y)

    @staticmethod
    def dist(v1, v2):
        return np.sqrt(np.power(v2.x-v1.x, 2) + np.power(v2.y-v1.y, 2))

    @staticmethod
    def random2D():
        return Vector(random.randint(-200, 200)/200, random.randint(-200, 200)/200)

    def set_angle(self, angle):
        magnitude = self.get_mag()
        self.x = np.cos(angle) * magnitude
        self.y = np.sin(angle) * magnitude
        return self

    def divide(self, div):
        self.x /= div
        self.y /= div
        return self
