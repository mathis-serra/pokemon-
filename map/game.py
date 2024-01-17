import pygame
<<<<<<< HEAD:map/game.py
from keyhandler import KeyListener
from map.map import Map
from map.player import Player
from screen import Screen
=======
from Keyhandler import KeyListener
from Map import Map
from Player import Player
from Screen import Screen
>>>>>>> map:game.py


class Game:
    def __init__(self):
        self.running: bool = True
        self.screen: Screen = Screen()
        self.map: Map = Map(self.screen)
        self.keylistener: KeyListener = KeyListener()
        self.player: Player = Player(self.keylistener, self.screen, 512, 288)
        self.map.add_player(self.player)

    def run(self) -> None:
        while self.running:
            self.handle_input()
            self.map.update()
            self.screen.update()

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.keylistener.add_key(event.key)
            elif event.type == pygame.KEYUP:
                self.keylistener.remove_key(event.key)