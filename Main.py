from Vehicle import *
import pygame

pygame.init()
WIDTH = 640
HEIGHT = 480
FPS = 60
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()


vehicle = Vehicle(screen, WIDTH/2, HEIGHT/2)
target = Target(screen, random.randint(0, WIDTH), random.randint(0, HEIGHT))


running = True
while running:
    clock.tick(FPS)
    # BACKGROUND
    screen.fill(color=(20, 20, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mx, my = pygame.mouse.get_pos()
    target = Vector(mx, my)
    # pygame.draw.circle(screen, (255, 0, 0), (target.x, target.y), 10)

    steering = vehicle.arrive(target)
    vehicle.apply_force(steering)

    # d = Vector.dist(vehicle.pos, target.pos)
    # if d < vehicle.r + target.r:
    #     target = Target(screen, random.randint(0, WIDTH), random.randint(0, HEIGHT))
    #     vehicle.pos.set(WIDTH/2, HEIGHT/2)

    # target.edges(WIDTH, HEIGHT)
    # target.update()
    # target.draw()
    pygame.draw.circle(screen, (255, 0, 0), (target.x, target.y), 10)

    vehicle.update()
    vehicle.draw()
    vehicle.edges(WIDTH, HEIGHT)

    pygame.display.flip()

pygame.quit()
