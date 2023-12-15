"""Base class for all menus"""


import pygame


class Menu:
    """Base class for all menus"""
    def __init__(self, screen):
        try:
            self.screen = screen
            self.title_font = pygame.font.Font('fonts/Roboto-Bold.ttf', 50)
            self.option_font = pygame.font.Font('fonts/Roboto-Italic.ttf', 40)

        except pygame.error as e:
            print("Ошибка при загрузке шрифта:", e)
            # Можно добавить дополнительные действия в случае ошибки, например, завершение программы
            pygame.quit()
            exit()