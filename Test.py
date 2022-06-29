
import pygame
from pygame.locals import *
pygame.init()   

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("USE {WASD} or {ARROW KEYS} TO MOVE & {ESCAPE} TO CLOSE")

clock = pygame.time.Clock()

#player = pygame.Surface((20, 20))
#player.fill((255,255,255))


pos1 = 100
pos2 = 100

print("HI I MADE THIS - LIzard")
print("https://github.com/LIzardLoser/FirstPythonCode")



run = True
while run:

    pygame.font.init()
    fontSize = 40
    font = pygame.font.SysFont('Comic Sans MS',fontSize)


    WIN.fill((0,0,0))

    villian = pygame.draw.rect(WIN , (255,0,0), (200,200,20,20))
    player = pygame.draw.rect(WIN , (255,255,255), (pos1,pos2,20,20))

    player #player
    villian #villian

    if villian.colliderect(player):
        pygame.display.set_caption("DED")
        label = font.render("YOU DID THE DIE", False, (255,255,255))
        WIN.blit(label,(0,0))

    clock.tick(60)
    #WIN.blit(villian, (200, 200))
    #WIN.blit(player, (pos1, pos2))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not villian.colliderect(player) or event.key == pygame.K_a and not villian.colliderect(player):
                pos1 -= 5
                break
            if event.key == pygame.K_RIGHT and not villian.colliderect(player) or event.key == pygame.K_d and not villian.colliderect(player):
                pos1 += 5
                break
            if event.key == pygame.K_UP and not villian.colliderect(player) or event.key == pygame.K_w and not villian.colliderect(player):
                pos2 -=5
                break
            if event.key == pygame.K_DOWN and not villian.colliderect(player) or event.key == pygame.K_s and not villian.colliderect(player):
                pos2 += 5
                break  
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                break
            break
        

pygame.quit()