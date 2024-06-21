from Models.Player import Player
from Controllers.GameController import GameController
from Controllers.CellController import CellController
import pygame

player_1 = Player(1, 0, (255, 0, 0))
player_2 = Player(2, 1, (0, 0, 255))

Column = input("Combien de colonnes souhaitez-vous ?")
Column = int(Column)

Size = input("Quelle taille des cases souhaitez-vous ?")
Size = int(Size)

Alignment = input("Combien de symboles souhaitez-vous alignez ?")
Alignment = int(Alignment)

GameController = GameController(Column, Size)
GameController.AddPlayer(player_1)
GameController.AddPlayer(player_2)

GameController.StartGame()

CellController = CellController()

Game = True
while Game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = CellController.OnClick(event)
            GameController.TryPlay(mouse_x, mouse_y)
    if GameController.IsWinnerRow(Alignment) is not None :
        Game = False


