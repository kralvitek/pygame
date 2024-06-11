import pygame 

pygame.init()

width = 600
height = 300
screen =pygame.display.set_mode((width, height))
pygame.display.set_caption("naše první hra")

player = pygame.Rect((300, 250, 50, 50))

lets_continue = True

clock = pygame.time.clock()



while lets_continue:
    screen.fill((0,0,0))
    pygame.draw.Rect(screen,(255, 0, 0), player)

    key = pygame.key.get_pressed()
 
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
 
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
 
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
 
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
 
    for event in pygame.event.get():
        print(event)
       
        if event.type == pygame.QUIT:
            lets_continue = False
 
pygame.display.update()
 
# Ukončení pygame
pygame.quit()