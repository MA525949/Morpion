import pygame
import sys
from pygame.locals import *
vitesse_x = 2
vitesse_y = 2
vitesse_x2 = 4
vitesse_y2 = 3
terrain1 = pygame.image.load('terrain1.jpg')
backgroundlist = [terrain1]
size = terrain1.get_rect()
window_size = (size.w, size.h)
screen = pygame.display.set_mode(window_size)
couleur = 1


def load_background_image(i=0):
    return backgroundlist[i]


for i in range(1):
    screen.blit(backgroundlist[i], (i * 10, 0))
playerpos = 0
playerimage = pygame.image.load('player.png')
playerimagebleu = pygame.image.load('playerbleu.png')
playerimagerose = pygame.image.load('playerrose.png')
playerimagejaune = pygame.image.load('playerjaune.png')
playerimagevert = pygame.image.load('playervert.png')
positionplayer = playerimagebleu.get_rect()
positionplayer2 = playerimage.get_rect()
backgroundlist = load_background_image()
screen.blit(backgroundlist, (0, 0))
position = playerimagebleu.get_rect()
position2 = playerimage.get_rect()
clock = pygame.time.Clock()
while (True) :                   #animate 100 frames
    screen.blit(backgroundlist, position, position)
    screen.blit(backgroundlist, position2, position2)#erase
    position = position.move(vitesse_x, vitesse_y)
    position2 = position.move(vitesse_x2, vitesse_y2)#move player
    if couleur == 1 :
        screen.blit(playerimagebleu, position)
    elif couleur == 2:
        screen.blit(playerimagejaune, position)
    elif couleur == 3:
        screen.blit(playerimagevert, position)
    else :
        screen.blit(playerimagerose, position)
    screen.blit(playerimage, position2)
    clock.tick(60)
    if position[0]+positionplayer.h+190>size.w or position[0]<0 :
        vitesse_x=-vitesse_x
        if couleur != 4 :
            couleur = couleur+1
        else :
            couleur = 1
    if position[1]+positionplayer.w-190>size.h or position[1]<0 :
        vitesse_y=-vitesse_y
        if couleur != 4 :
            couleur = couleur+1
        else :
            couleur = 1
    if position2[0]+positionplayer2.h+190>size.w or position2[0]<0 :
        vitesse_x2=-vitesse_x2
    if position2[1]+positionplayer2.w-190>size.h or position2[1]<0 :
        vitesse_y2=-vitesse_y2


