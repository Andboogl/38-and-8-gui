"""Base class for all menus"""


import pygame


class BaseMenu:
    """Base class for all menus"""
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font('fonts/Roboto-Bold.ttf', 50)
        self.option_font = pygame.font.Font('fonts/Roboto-Italic.ttf', 40)
