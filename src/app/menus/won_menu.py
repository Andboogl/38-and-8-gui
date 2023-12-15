"""Won menu"""


import pygame
from .base import Menu


class WonMenu(Menu):
    """Won menu"""
    def draw(self):
        """Draw won menu"""
        self.screen.fill((0, 0, 0))

        # Title
        title_text = self.title_font.render('You won!', True, (240, 240, 245))
        self.screen.blit(title_text, (300, 10))

        # Play again
        play_again_text = self.option_font.render('Play again', True, (240, 240, 245))
        play_again_rect = play_again_text.get_rect(topleft=(310, 84))
        self.screen.blit(play_again_text, (310, 84))

        # Main menu
        main_menu_text = self.option_font.render('Main menu', True, (240, 240, 245))
        main_menu_rect = main_menu_text.get_rect(topleft=(300, 130))
        self.screen.blit(main_menu_text, (300, 130))

        # Pressing text
        if play_again_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return 'New game'

        # Pressing text
        if main_menu_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return 'Main menu'

        return 'Won'
