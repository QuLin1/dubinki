import pygame
pygame.init()
window = pygame.display.set_mode((1240, 960))
window.fill((255, 0 ,55))
clock = pygame.time.Clock()
run = True
while run:
    for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
    clock.tick(60)
    pygame.display.update()