"""Play menu"""


import pygame
import objects
from .map_coordinates import coordinates
from ..utils import Timer, BaseMenu


class PlayMenu(BaseMenu):
    """Play menu"""
    def init(self):
        # Creating board and position
        self.board = objects.Board(8, 8)

        coor = objects.generate_coordinates(7, 7, 20)
        self.player = objects.Player(*coor[5])
        point = objects.Point(*coor[0])
        point2 = objects.Point(*coor[1])
        point3 = objects.Point(*coor[2])
        point4 = objects.Point(*coor[3])
        point5 = objects.Point(*coor[4])
        point6 = objects.Point(*coor[16])
        point7 = objects.Point(*coor[17])
        point8 = objects.Point(*coor[18])
        point9 = objects.Point(*coor[19])
        point10 = objects.Point(*coor[20])
        obstacle1 = objects.Obstacle(*coor[6])
        obstacle2 = objects.Obstacle(*coor[7])
        obstacle3 = objects.Obstacle(*coor[8])
        obstacle4 = objects.Obstacle(*coor[9])
        obstacle5 = objects.Obstacle(*coor[10])
        obstacle6 = objects.Obstacle(*coor[11])
        obstacle7 = objects.Obstacle(*coor[12])
        obstacle8 = objects.Obstacle(*coor[13])
        obstacle9 = objects.Obstacle(*coor[14])
        obstacle10 = objects.Obstacle(*coor[15])

        self.board.put_figures(
            point, point2, point3, point4, point5, point6,
            point7, point8, point9, point10,
            obstacle1, obstacle2, obstacle3, obstacle4,
            obstacle5, obstacle6, obstacle7, obstacle8,
            obstacle9, obstacle10, self.player)

        self.map_objects = {
            f'{point.x}:{point.y}': pygame.transform.scale(pygame.image.load('images/point.png'), (24, 24)),
            f'{point2.x}:{point2.y}': pygame.transform.scale(pygame.image.load('images/point.png'), (24, 24)),
            f'{point3.x}:{point3.y}': pygame.transform.scale(pygame.image.load('images/point.png'), (24, 24)),
            f'{point4.x}:{point4.y}': pygame.transform.scale(pygame.image.load('images/point.png'), (24, 24)),
            f'{point5.x}:{point5.y}': pygame.transform.scale(pygame.image.load('images/point.png'), (24, 24)),
            f'{point6.x}:{point6.y}': pygame.transform.scale(pygame.image.load('images/point.png'), (24, 24)),
            f'{point7.x}:{point7.y}': pygame.transform.scale(pygame.image.load('images/point.png'), (24, 24)),
            f'{point8.x}:{point8.y}': pygame.transform.scale(pygame.image.load('images/point.png'), (24, 24)),
            f'{point9.x}:{point9.y}': pygame.transform.scale(pygame.image.load('images/point.png'), (24, 24)),
            f'{point10.x}:{point10.y}': pygame.transform.scale(pygame.image.load('images/point.png'), (24, 24)),
            f'{obstacle1.x}:{obstacle1.y}': pygame.transform.scale(pygame.image.load('images/obstacle.png'), (24, 24)),
            f'{obstacle2.x}:{obstacle2.y}': pygame.transform.scale(pygame.image.load('images/obstacle.png'), (24, 24)),
            f'{obstacle3.x}:{obstacle3.y}': pygame.transform.scale(pygame.image.load('images/obstacle.png'), (24, 24)),
            f'{obstacle4.x}:{obstacle4.y}': pygame.transform.scale(pygame.image.load('images/obstacle.png'), (24, 24)),
            f'{obstacle5.x}:{obstacle5.y}': pygame.transform.scale(pygame.image.load('images/obstacle.png'), (24, 24)),
            f'{obstacle6.x}:{obstacle6.y}': pygame.transform.scale(pygame.image.load('images/obstacle.png'), (24, 24)),
            f'{obstacle7.x}:{obstacle7.y}': pygame.transform.scale(pygame.image.load('images/obstacle.png'), (24, 24)),
            f'{obstacle8.x}:{obstacle8.y}': pygame.transform.scale(pygame.image.load('images/obstacle.png'), (24, 24)),
            f'{obstacle9.x}:{obstacle9.y}': pygame.transform.scale(pygame.image.load('images/obstacle.png'), (24, 24)),
            f'{obstacle10.x}:{obstacle10.y}': pygame.transform.scale(pygame.image.load('images/obstacle.png'), (24, 24)),
            f'{self.player.x}:{self.player.y}': pygame.transform.scale(pygame.image.load('images/player.png'), (24, 24))
        }

        Timer
        self.timer = Timer()
        self.timer.set_start_to_current()

    def draw(self):
        """Draw play menu on the screen"""
        self.screen.fill((0, 0, 0))

        map_image = pygame.image.load('images/map.png')
        self.screen.blit(map_image, (0, 0))

        # options_font = pygame.font.Font('fonts/Roboto-Bold.ttf', 30)

        # Back
        back_text = self.option_font.render('Back', True, (240, 240, 245))
        back_text_area = back_text.get_rect(topleft=(14, 8))
        self.screen.blit(back_text, (14, 8))

        # Points collected
        points_collected = self.option_font.render(f'{self.player.points_collected}/10', True, (240, 240, 245))
        self.screen.blit(points_collected, (690, 8))

        # Points left
        points_left = self.option_font.render(f'{self.board.count_of_points()} points left', True, (240, 240, 245))
        self.screen.blit(points_left, (565, 56))

        # Count of player moves
        player_moves = self.option_font.render(f'{self.player.moves_count} moves', True, (240, 240, 245))
        self.screen.blit(player_moves, (615, 96))

        # Playing time in seconds
        play_time = self.option_font.render(f'{int(self.timer.end)} seconds', True, (240, 240, 245))
        self.screen.blit(play_time, (600, 145))

        # Drawing objects
        for coordinate, image in self.map_objects.items():
            self.screen.blit(image, coordinates[coordinate])

        # If user clicked back
        if back_text_area.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return 'Main menu'

        # If user won
        if self.board.is_win():
            return f'Won {self.player.moves_count} {int(self.timer.end)}'

        return 'Playing'
