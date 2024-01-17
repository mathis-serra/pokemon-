import pygame
from screen import Screen
from Settings import Settings
from Settings import *
from Sprites import Sprites
from Button import Button
from map.game import Game
import combat.main as main
import sys
import combat.main as main
from Button import Button

class Menu():
    
    def __init__(self):
        pygame.init()
        
        self.SCREEN = Screen()
        self.SETTINGS = Settings()
    
    
    def main_menu(self):
        font = pygame.font.Font("Data/Game/Font/pokemon-emerald.ttf", 36)
        self.SCREEN.display.blit(self.SPRITES.main_menu_pokemon, (0, 0))
        new_game_button = Button(160, 60, self.SPRITES.menu_bar_pokemon, 1) 
        continue_button = Button(160, 150, self.SPRITES.menu_bar_pokemon, 1) 
        mysyery_gift_button = Button(160, 240, self.SPRITES.menu_bar_pokemon, 1) 
        settings_button = Button(160, 330, self.SPRITES.menu_bar_pokemon, 1)
        pokedex_button = Button(160, 420, self.SPRITES.menu_bar_pokemon, 1) 
        self.SCREEN.display.blit(self.SPRITES.menu_bar_pokemon, (160, 510))
        
        new_game_button.draw(self.SCREEN.display)
        continue_button.draw(self.SCREEN.display)
        mysyery_gift_button.draw(self.SCREEN.display)
        settings_button.draw(self.SCREEN.display)
        pokedex_button.draw(self.SCREEN.display)
        
        text_surface = font.render("NEW GAME", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(645, 102))
        text_surface2 = font.render("CONTINUE", True, (255, 255, 255))
        text_rect2 = text_surface2.get_rect(center=(645, 192))
        text_surface3 = font.render("MYSTERY GIFT", True, (255, 255, 255))
        text_rect3 = text_surface3.get_rect(center=(645, 282))
        text_surface4 = font.render("SETTINGS", True, (255, 255, 255))
        text_rect4 = text_surface4.get_rect(center=(645, 372))
        text_surface5 = font.render("POKEDEX", True, (255, 255, 255))
        text_rect5= text_surface4.get_rect(center=(645, 462))
        
        self.SCREEN.display.blit(text_surface, text_rect)
        self.SCREEN.display.blit(text_surface2, text_rect2)
        self.SCREEN.display.blit(text_surface3, text_rect3)
        self.SCREEN.display.blit(text_surface4, text_rect4)
        self.SCREEN.display.blit(text_surface5, text_rect5)
        # self.SCREEN.update()
        
        
            

    def run(self):
        self.SPRITES = Sprites()
        self.main_menu()
        
        selected_button = "new_game_button"
        
        menu_buttons = {
        "new_game_button": Button(160, 60, self.SPRITES.menu_bar_pokemon, 1),
        "continue_button": Button(160, 150, self.SPRITES.menu_bar_pokemon, 1),
        "mysyery_gift_button": Button(160, 240, self.SPRITES.menu_bar_pokemon, 1),
        "settings_button": Button(160, 330, self.SPRITES.menu_bar_pokemon, 1),
        "pokedex_button": Button(160, 420, self.SPRITES.menu_bar_pokemon, 1),
        }
        
        while True:
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if selected_button in menu_buttons and menu_buttons[selected_button].draw(self.SCREEN.display):
                        self.SCREEN.display.fill((0, 0, 0))
                        pygame.display.flip()
                    if selected_button == "new_game_button":
                        game = Game()
                        game.run()
                                        
                    if selected_button == "continue_button" :
                        self.SCREEN.display.fill((0, 0, 0))
                        pygame.display.update()
                        main()
                        self.main_menu()
                        
                    if selected_button == "mysyery_gift_button" :
                        self.SCREEN.display.fill((0, 0, 0))
                        pygame.display.update()
                        main()
                        self.main_menu()
                        
                    if selected_button == "settings_button" :
                        self.SCREEN.display.fill((0, 0, 0))
                        pygame.display.update()
                        main()
                        self.main_menu()
                        
                    if selected_button == "pokedex_button" :
                        self.SCREEN.display.fill((0, 0, 0))
                        pygame.display.update()
                        main()
                        self.main_menu()
           
            pygame.display.update()      
            
            
        

            
            
            
