import pygame
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption('Sin And Cos Simulation')

done = False

screen.fill(BLACK)
SinX = 1
CosX = 1
SinY = math.sin(SinX)
CosY = math.cos(CosX)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, WHITE, (SinX, SinY-100, 2, 2))
    pygame.draw.rect(screen, RED, (CosX, CosY+1100, 2, 2))

    SinY += math.sin(math.radians(SinX))
    CosY += math.cos(math.radians(CosX))

    SinX += 0.5
    CosX += 0.5

    if CosX >= 1000:
        CosX = 0
    elif SinY >= 1000:
        SinY = 0
    elif SinX >= 1000:
        SinX = 0

    pygame.display.flip()

pygame.quit()