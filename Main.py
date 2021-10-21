from Vehicle import *
from Path import *
import pygame

pygame.init()
WIDTH = 640
HEIGHT = 480
FPS = 60
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()


vehicle = Vehicle(screen, WIDTH/2, HEIGHT/2)
target = Target(screen, random.randint(0, WIDTH), random.randint(0, HEIGHT))
path = Path(screen, Vector(0, HEIGHT/2), Vector(WIDTH, HEIGHT/2))


running = True
toggle = False
while running:
    clock.tick(FPS)
    # BACKGROUND
    screen.fill(color=(20, 20, 30))

    path.draw(draw_radius=toggle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                toggle = not toggle

    mx, my = pygame.mouse.get_pos()
    path.end.y = my
    target = Vector(mx, my)
    # pygame.draw.circle(screen, (255, 0, 0), (target.x, target.y), 10)

    # steering = vehicle.arrive(target)
    # vehicle.apply_force(steering)
    # steering1 = vehicle.wander(0.5, draw=False)    # wander
    steering2 = vehicle.follow(path, draw=toggle)
    # vehicle.apply_force(steering1)
    vehicle.apply_force(steering2)

    # d = Vector.dist(vehicle.pos, target.pos)
    # if d < vehicle.r + target.r:
    #     target = Target(screen, random.randint(0, WIDTH), random.randint(0, HEIGHT))
    #     vehicle.pos.set(WIDTH/2, HEIGHT/2)

    # target.edges(WIDTH, HEIGHT)
    # target.update()
    # target.draw()
    # pygame.draw.circle(screen, (255, 0, 0), (target.x, target.y), 10)

    vehicle.update()
    vehicle.draw(draw_vectors=False, draw_path=False)
    vehicle.edges(WIDTH, HEIGHT)

    pygame.display.flip()

pygame.quit()
