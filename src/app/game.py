"""Game"""


import pygame
from . import menus
from .utils import Records


class Game:
    """Game"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('38-and-8 gui 1.5.0')

        self.play_mode = 'Main menu'
        self.records = Records()

        # Menus
        self.main_menu = menus.MainMenu(self.screen)
        self.won_menu = menus.WonMenu(self.screen)

    def main_loop(self):
        """Game main loop"""
        while True:
            if self.play_mode == 'Main menu':
                self.play_mode = self.main_menu.draw()

            elif self.play_mode == 'Won':
                self.play_mode = self.won_menu.draw(
                    moves_count, seconds_count,
                    self.records.best_record()['moves'],
                    self.records.best_record()['seconds'])

            elif self.play_mode == 'New game':
                self.play_menu = menus.PlayMenu(self.screen)
                self.play_menu.init()
                self.play_mode = 'Playing'

            elif self.play_mode == 'Playing':
                self.play_mode = self.play_menu.draw()

                if self.play_mode.startswith('Won'):
                    moves_count = self.play_mode.split(' ')[1]
                    seconds_count = self.play_mode.split(' ')[2]
                    self.records.load_record(moves_count, seconds_count)
                    self.play_mode = 'Won'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)

                if self.play_mode == 'Playing':
                    if event.type == pygame.KEYDOWN:
                        obstacles = self.play_menu.board.count_of_obstacles()
                        points = self.play_menu.board.count_of_points()
                        move_done = False

                        # Moving to left
                        if event.key == pygame.K_a:
                            if [self.play_menu.player.x, self.play_menu.player.y - 1] in self.play_menu.player.get_moves(self.play_menu.board):
                                self.play_menu.map_objects[f'{self.play_menu.player.x}:{self.play_menu.player.y - 1}'] = self.play_menu.map_objects[
                                    f'{self.play_menu.player.x}:{self.play_menu.player.y}']
                                self.play_menu.map_objects.pop(f'{self.play_menu.player.x}:{self.play_menu.player.y}')
                                self.play_menu.board.move_player(self.play_menu.player, [self.play_menu.player.x, self.play_menu.player.y - 1])
                                move_done = True

                        # Moving to right
                        elif event.key == pygame.K_d:
                            if [self.play_menu.player.x, self.play_menu.player.y + 1] in self.play_menu.player.get_moves(
                                    self.play_menu.board):
                                self.play_menu.map_objects[f'{self.play_menu.player.x}:{self.play_menu.player.y + 1}'] = self.play_menu.map_objects[
                                    f'{self.play_menu.player.x}:{self.play_menu.player.y}']
                                self.play_menu.map_objects.pop(f'{self.play_menu.player.x}:{self.play_menu.player.y}')
                                self.play_menu.board.move_player(self.play_menu.player,
                                                                 [self.play_menu.player.x, self.play_menu.player.y + 1])
                                move_done = True

                        # Moving to up
                        elif event.key == pygame.K_w:
                            if [self.play_menu.player.x - 1, self.play_menu.player.y] in self.play_menu.player.get_moves(
                                    self.play_menu.board):
                                self.play_menu.map_objects[f'{self.play_menu.player.x - 1}:{self.play_menu.player.y}'] = self.play_menu.map_objects[
                                    f'{self.play_menu.player.x}:{self.play_menu.player.y}']
                                self.play_menu.map_objects.pop(f'{self.play_menu.player.x}:{self.play_menu.player.y}')
                                self.play_menu.board.move_player(self.play_menu.player,
                                                                 [self.play_menu.player.x - 1, self.play_menu.player.y])
                                move_done = True

                        # Moving to down
                        elif event.key == pygame.K_s:
                            if [self.play_menu.player.x + 1, self.play_menu.player.y] in self.play_menu.player.get_moves(
                                    self.play_menu.board):
                                self.play_menu.map_objects[f'{self.play_menu.player.x + 1}:{self.play_menu.player.y}'] = self.play_menu.map_objects[
                                    f'{self.play_menu.player.x}:{self.play_menu.player.y}']
                                self.play_menu.map_objects.pop(f'{self.play_menu.player.x}:{self.play_menu.player.y}')
                                self.play_menu.board.move_player(self.play_menu.player,
                                                                 [self.play_menu.player.x + 1, self.play_menu.player.y])
                            move_done = True

                        if move_done:
                            # Playing sound
                            if self.play_menu.board.count_of_obstacles() < obstacles:
                                pygame.mixer.Sound('sounds/obstacle_destroy.mp3').play()

                            elif self.play_menu.board.count_of_points() < points:
                                pygame.mixer.Sound('sounds/point.mp3').play()

                            else:
                                pygame.mixer.Sound('sounds/move.mp3').play()

            pygame.display.update()
