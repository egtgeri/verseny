import csv
import pygame

#fájl beolvasása
#with open('mars_map_50x50.csv', newline="\n", encoding = 'utf-8') as f:
 #   kockak = csv.reader(f, delimiter=',')
  #  print(kockak)
   # for row in kockak:
    #    print(*row)

    

pygame.init()

screen = pygame.display.set_mode((1280,900))
image1 = pygame.image.load("img/mars_rover.png").convert_alpha() 
image1= pygame.transform.scale(image1,(image1.get_width()/5,image1.get_height()/5))

clock = pygame.time.Clock()

running = True

while running:
    screen.fill((255,255,255))
   # pygame.display.flip()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(image1,(100,100))
    pygame.display.update()

pygame.quit







