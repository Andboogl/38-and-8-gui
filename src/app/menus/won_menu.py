"""Won menu"""


import pygame
from ..utils import BaseMenu


class WonMenu(BaseMenu):
    """Won menu"""
    def draw(self,
             moves_count, seconds_count,
             record_moves, record_seconds):
        """Draw won menu"""
        self.screen.fill((0, 0, 0))

        # Title
        title_text = self.title_font.render(f'You won!', True, (240, 240, 245))
        self.screen.blit(title_text, (800 / 2 - title_text.get_width() / 2, 7))

        # Moves count
        moves_text = self.option_font.render(f'{moves_count} moves', True, (240, 240, 245))
        self.screen.blit(moves_text, (800 / 2 - moves_text.get_width() / 2, 85))

        # Seconds count
        seconds_text = self.option_font.render(f'{int(seconds_count)} seconds', True, (240, 240, 245))
        self.screen.blit(seconds_text, (800 / 2 - seconds_text.get_width() / 2, 140))

        # Record
        record_title = self.option_font.render('Record', True, (240, 240, 245))
        self.screen.blit(record_title, (30, 85))

        record_moves = self.option_font.render(f'{record_moves} moves', True, (240, 240, 245))
        record_seconds = self.option_font.render(f'{record_seconds} seconds', True, (240, 240, 245))
        self.screen.blit(record_moves, (30, 130))
        self.screen.blit(record_seconds, (30, 170))

        # Play again
        play_again_text = self.option_font.render('Play again', True, (240, 240, 245))
        play_again_rect = play_again_text.get_rect(topleft=(214, 312))
        self.screen.blit(play_again_text, (214, 312))

        # Main menu
        main_menu_text = self.option_font.render('Main menu', True, (240, 240, 245))
        main_menu_rect = main_menu_text.get_rect(topleft=(430, 312))
        self.screen.blit(main_menu_text, (430, 312))

        # Pressing text
        if play_again_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return 'New game'

        # Pressing text
        if main_menu_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return 'Main menu'

        return 'Won'
