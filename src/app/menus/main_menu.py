"""Main menu"""


import pygame
from ..utils import BaseMenu


class MainMenu(BaseMenu):
    """Main menu"""
    def draw(self):
        """Draw main menu"""
        self.screen.fill((0, 0, 0))

        # Title
        self.screen.blit(
            self.title_font.render(
                '38-and-8 gui',
                True,
                (240, 240, 245)),
            (250, 10))

        # Play
        play_text = self.option_font.render('Play', True, (240, 240, 245))
        play_text_area = play_text.get_rect(topleft=(350, 100))
        self.screen.blit(
            play_text,
            (350, 100))

        if play_text_area.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return 'New game'

        return 'Main menu'
