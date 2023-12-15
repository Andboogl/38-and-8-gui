"""Game"""


import pygame
from . import menus


class Game:
    """Game"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('38-and-8 gui 1.2.0')

        self.play_mode = 'Main menu'

        # Menus
        self.main_menu = menus.MainMenu(self.screen)
        self.won_menu = menus.WonMenu(self.screen)

    def main_loop(self):
        """Game main loop"""
        while True:
            if self.play_mode == 'Main menu':
                self.play_mode = self.main_menu.draw()

            elif self.play_mode == 'Won':
                self.play_mode = self.won_menu.draw(self.moves_count)

            elif self.play_mode == 'New game':
                self.play_menu = menus.PlayMenu(self.screen)
                self.play_mode = 'Playing'

            elif self.play_mode == 'Playing':
                self.play_mode = self.play_menu.draw()

                if self.play_mode.startswith('Won'):
                    self.moves_count = self.play_mode.split(' ')[1]
                    self.play_mode = 'Won'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)

                if self.play_mode == 'Playing':
                    if event.type == pygame.KEYDOWN:
                        # Moving to left
                        if event.key == pygame.K_a:
                            if [self.play_menu.player.x, self.play_menu.player.y - 1] in self.play_menu.player.get_moves(self.play_menu.board):
                                self.play_menu.map_objects[f'{self.play_menu.player.x}:{self.play_menu.player.y - 1}'] = self.play_menu.map_objects[
                                    f'{self.play_menu.player.x}:{self.play_menu.player.y}']
                                self.play_menu.map_objects.pop(f'{self.play_menu.player.x}:{self.play_menu.player.y}')
                                self.play_menu.board.move_player(self.play_menu.player, [self.play_menu.player.x, self.play_menu.player.y - 1])

                        # Moving to right
                        if event.key == pygame.K_d:
                            if [self.play_menu.player.x, self.play_menu.player.y + 1] in self.play_menu.player.get_moves(
                                    self.play_menu.board):
                                self.play_menu.map_objects[f'{self.play_menu.player.x}:{self.play_menu.player.y + 1}'] = self.play_menu.map_objects[
                                    f'{self.play_menu.player.x}:{self.play_menu.player.y}']
                                self.play_menu.map_objects.pop(f'{self.play_menu.player.x}:{self.play_menu.player.y}')
                                self.play_menu.board.move_player(self.play_menu.player,
                                                                 [self.play_menu.player.x, self.play_menu.player.y + 1])
                        # Moving to up
                        if event.key == pygame.K_w:
                            if [self.play_menu.player.x - 1, self.play_menu.player.y] in self.play_menu.player.get_moves(
                                    self.play_menu.board):
                                self.play_menu.map_objects[f'{self.play_menu.player.x - 1}:{self.play_menu.player.y}'] = self.play_menu.map_objects[
                                    f'{self.play_menu.player.x}:{self.play_menu.player.y}']
                                self.play_menu.map_objects.pop(f'{self.play_menu.player.x}:{self.play_menu.player.y}')
                                self.play_menu.board.move_player(self.play_menu.player,
                                                                 [self.play_menu.player.x - 1, self.play_menu.player.y])
                        # Moving to down
                        if event.key == pygame.K_s:
                            if [self.play_menu.player.x + 1, self.play_menu.player.y] in self.play_menu.player.get_moves(
                                    self.play_menu.board):
                                self.play_menu.map_objects[f'{self.play_menu.player.x + 1}:{self.play_menu.player.y}'] = self.play_menu.map_objects[
                                    f'{self.play_menu.player.x}:{self.play_menu.player.y}']
                                self.play_menu.map_objects.pop(f'{self.play_menu.player.x}:{self.play_menu.player.y}')
                                self.play_menu.board.move_player(self.play_menu.player,
                                                                 [self.play_menu.player.x + 1, self.play_menu.player.y])

            pygame.display.update()
