import pygame


class Screen:
    def __init__(self, size_width, size_height):
        self.size_width = size_width
        self.size_height = size_height

    @classmethod
    def OpenScreen(cls, size_width, size_height):
        screen = pygame.display.set_mode((size_width, size_height))
