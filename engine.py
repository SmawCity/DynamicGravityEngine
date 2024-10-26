import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basic Physics Simulation")

GRAY = (44, 44, 44)
RED = (255, 0, 0)

position = pygame.Vector2(400, 50)  
velocity = pygame.Vector2(0, 0) 
acceleration = pygame.Vector2(0, 0.5) 
radius = 20  
restitution = 0.8  

clock = pygame.time.Clock()
fps = 60  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    velocity += acceleration
    position += velocity

    # Ground collision
    if position.y + radius > height:
        position.y = height - radius  
        velocity.y *= -restitution 

    screen.fill(GRAY)
    pygame.draw.circle(screen, RED, (int(position.x), int(position.y)), radius)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()