import pygame
pygame.init()


class CellController:

    def OnClick(self, event):
        if event.button == 1:
            mouse_pos = event.pos
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos

