"""Aplication package"""


from .game import Game


def run_game():
    """Run game"""
    game = Game()
    game.main_loop()
