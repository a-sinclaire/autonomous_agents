from Vector import *
import pygame.draw
import numpy as np


def map_range(value, min1, max1, min2, max2):
    slope = (max2 - min2) / (max1 - min1)
    return min2 + (slope * (value - min1))


class Vehicle:
    def __init__(self, surface, x, y):
        self.surface = surface
        self.color = (255, 255, 0)
        self.pos = Vector(x, y)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.maxSpeed = 6
        self.maxForce = 0.5
        self.r = 16
        self.wander_angle = random.randint(0, round(np.pi*200))/100

    def seek(self, target, arrive=False):
        force = Vector.static_sub(target, self.pos)
        desired_speed = self.maxSpeed
        if arrive:
            slow_radius = 100
            d = force.get_mag()
            if d < slow_radius:
                desired_speed = map_range(d, 0, slow_radius, 0, self.maxSpeed)

        force.set_mag(desired_speed)
        force.sub(self.vel)
        force.limit(self.maxForce)
        return force

    def flee(self, target):
        return self.seek(target).mult(-1)

    def pursue(self, vehicle):
        target = vehicle.pos.copy()
        prediction = vehicle.vel.copy()

        # how far to look in future?
        f = Vector.dist(self.pos, target)
        f /= 8

        prediction.mult(f)
        target.add(prediction)
        # pygame.draw.circle(self.surface, (0, 255, 0), (target.x, target.y), 5)
        return self.seek(target)

    def evade(self, vehicle):
        pursuit = self.pursue(vehicle)
        pursuit.mult(-1)
        return pursuit

    def arrive(self, target):
        return self.seek(target, arrive=True)

    def wander(self):
        circle_distance = self.r*np.sqrt(2)
        circle_center = self.vel.copy()
        circle_center.normalize()
        circle_center.mult(circle_distance)

        circle_radius = self.r
        displacement = Vector(0, -1)
        displacement.mult(circle_radius)

        # pygame.draw.circle(self.surface, (0, 255, 0), (circle_center.x + self.pos.x, circle_center.y + self.pos.y), circle_radius)

        displacement.set_angle(self.wander_angle)
        # angle_change in range 0-1 (turning strength)
        angle_change = 0.6
        self.wander_angle += (random.random() * angle_change) - (angle_change * 0.5)

        # pygame.draw.circle(self.surface, (255, 0, 0), (circle_center.x + self.pos.x + displacement.x, circle_center.y + self.pos.y + displacement.y), 5)

        wander_force = circle_center.add(displacement)
        wander_force.limit(self.maxForce)
        return wander_force

    def apply_force(self, force):
        self.acc.add(force)

    def update(self):
        self.vel.add(self.acc)
        self.vel.limit(self.maxSpeed)
        self.pos.add(self.vel)
        self.acc.set(0, 0)

    def draw(self):
        ang = self.vel.get_heading()
        w = 3*np.pi/4
        x = self.pos.x
        y = self.pos.y
        points = [(x+np.cos(ang)*self.r, y+np.sin(ang)*self.r), (x+np.cos(ang+w)*self.r, y+np.sin(ang+w)*self.r), (x+np.cos(ang-w)*self.r, y+np.sin(ang-w)*self.r)]
        pygame.draw.polygon(self.surface, color=self.color, points=points)

    def edges(self, w, h):
        if self.pos.x < 0:
            self.pos.x = w
        if self.pos.x > w:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = h
        if self.pos.y > h:
            self.pos.y = 0


class Target(Vehicle):
    def __init__(self, surface, x, y):
        Vehicle.__init__(self, surface, x, y)
        self.vel = Vector.random2D()
        self.vel.mult(5)

    def draw(self):
        pygame.draw.circle(self.surface, (255, 0, 0), (self.pos.x, self.pos.y), self.r)
