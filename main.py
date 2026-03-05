import pygame
import csv

pygame.init()

screen = pygame.display.set_mode((1280, 900))
image1 = pygame.image.load("img/mars_rover.png").convert_alpha()

# Kép méretezése 50x50 pixelre
IMAGE_SIZE = 50
image1 = pygame.transform.scale(image1, (IMAGE_SIZE, IMAGE_SIZE))

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 50x50-es rács kirajzolása
    for row in range(50):  # sorok (y)
        for col in range(50):  # oszlopok (x)
            x = col * IMAGE_SIZE
            y = row * IMAGE_SIZE
            screen.blit(image1, (x, y))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
