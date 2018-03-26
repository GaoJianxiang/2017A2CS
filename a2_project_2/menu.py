from game import *
from functions import *
import pygame
from pygame.locals import *
from sys import exit
import os


class Menu:
    def __init__(self):
        self.background = load_image('menuBackground.png')

        self.game_buttons = load_image('play2.png', 2, [((x,0),(218, 197))\
                                             for x in range(0, 218, 218)])

        self.game_level = None
        self.car_type = 1

        self.game_button = self.game_buttons[0]
        self.game_size = self.game_button.get_size()
        self.game_pos = (0, 550)

        self.exit_buttons = load_image('sair.png', 2, [((x,0),(111,74))\
                                             for x in range(0, 333, 111)])
        self.exit_button = self.exit_buttons[0]
        self.exit_size = self.exit_button.get_size()
        self.exit_pos = (228, 125)


        self.back_buttons = load_image('voltar.png', 2, [((0,y),(134,36))\
                                             for y in range(0, 108, 36)])
        self.back_button = self.exit_buttons[0]
        self.back_size = self.exit_button.get_size()
        self.back_pos = (50, 720)

        self.pressed = False

        self.fullscreen = False

    def set_fullscreen(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LALT] and pressed_keys[K_RETURN]:
            self.fullscreen = not self.fullscreen

            if self.fullscreen:
                screen = pygame.display.set_mode((1024,768), FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode((1024,768), 0, 32)

    def main_menu(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('sounds' + os.sep + 'game_music.mp3')
        pygame.mixer.music.play()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()
            
            self.set_fullscreen()

            self.background = load_image('menuBackground.png')
            screen.blit(self.background, (0, 0))
                    

            # Operate if mouse clicks on these buttons
            # Play
            if self.game_pos[0] <= mouse_pos[0] <= self.game_pos[0] + self.game_size[0]\
            and self.game_pos[1] <= mouse_pos[1] <= self.game_pos[1] + self.game_size[1]:

                if mouse_press[0]:
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    pygame.mixer.music.stop()
                    self.select_car_menu()

            else: self.game_button = self.game_buttons[0]

            # Exit
            if self.exit_pos[0] <= mouse_pos[0] <= self.exit_pos[0] + self.exit_size[0]\
            and self.exit_pos[1] <= mouse_pos[1] <= self.exit_pos[1] + self.exit_size[1]:

                self.exit_button = self.exit_buttons[1]

                if mouse_press[0]:
                    self.exit_button = self.exit_buttons[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.exit_button = self.exit_buttons[1]
                    exit()

            else: self.exit_button = self.exit_buttons[0]

            if not mouse_press[0]:
                self.pressed = False

            #for button in menu.buttons:
            screen.blit(self.game_button, self.game_pos)
            screen.blit(self.exit_button, self.exit_pos)

            pygame.display.flip()


    def select_car_menu(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('sounds' + os.sep + 'select_menu.mp3')
        pygame.mixer.music.play()
        
        self.background = load_image('menuBackground.png')
        self.text = load_image('selectCar.png', 2)

        self.car_selected = None

        self.list_button1 = load_image('carro1_atributos.png', 2, [((0,y),(445,180))\
                                                        for y in range(0, 540, 180)])
        self.button1_image = self.list_button1[0]
        self.button1_pos = (50, 100)

        self.list_button2 = load_image('carro2_atributos.png', 2, [((0,y),(445,180))\
                                                        for y in range(0, 540, 180)])
        self.button2_image = self.list_button2[0]
        self.button2_pos = (250, 300)

        self.list_button3 = load_image('carro3_atributos.png', 2, [((0,y),(445,180))\
                                                        for y in range(0, 540, 180)])
        self.button3_image = self.list_button3[0]
        self.button3_pos = (450, 500)

        self.advance_images = load_image('select.png', 2, [((0,y),(150, 150))\
                                                for y in range(0, 150, 150)])
        self.advance_button = self.advance_images[0]
        self.advance_size = self.advance_button.get_size()
        self.advance_pos = (875, 600)
        
        self.a_car_size = self.button1_image.get_size()
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            self.set_fullscreen()

            screen.blit(self.background, (0, 0))

            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()

            if self.button1_pos[0] <= mouse_pos[0] <= self.button1_pos[0] + self.a_car_size[0]\
            and self.button1_pos[1] <= mouse_pos[1] <= self.button1_pos[1] + self.a_car_size[1]:
                self.button1_image = self.list_button1[1]

                if mouse_press[0]:
                    self.button1_image = self.list_button1[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.car_selected = 1

            elif self.car_selected == 1:
                self.button1_image = self.list_button1[1]
            else:
                self.button1_image = self.list_button1[0]


            if self.button2_pos[0] <= mouse_pos[0] <= self.button2_pos[0] + self.a_car_size[0]\
            and self.button2_pos[1] <= mouse_pos[1] <= self.button2_pos[1] + self.a_car_size[1]:
                self.button2_image = self.list_button2[1]

                if mouse_press[0]:
                    self.button2_image = self.list_button2[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.car_selected = 2

            elif self.car_selected == 2:
                self.button2_image = self.list_button2[1]
            else:
                self.button2_image = self.list_button2[0]


            if self.button3_pos[0] <= mouse_pos[0] <= self.button3_pos[0] + self.a_car_size[0]\
            and self.button3_pos[1] <= mouse_pos[1] <= self.button3_pos[1] + self.a_car_size[1]:
                self.button3_image = self.list_button3[1]

                if mouse_press[0]:
                    self.button3_image = self.list_button3[2]
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    self.car_selected = 3

            elif self.car_selected == 3:
                self.button3_image = self.list_button3[1]
            else:
                self.button3_image = self.list_button3[0]


            if self.advance_pos[0] <= mouse_pos[0] <= self.advance_pos[0] + self.advance_size[0]\
            and self.advance_pos[1] <= mouse_pos[1] <= self.advance_pos[1] + self.advance_size[1]:
                if mouse_press[0]:
                    self.pressed = True

                if self.pressed and not mouse_press[0]:
                    if self.car_selected is not None:
                        self.select_level_menu()

            else: self.advance_button = self.advance_images[0]


            if not mouse_press[0]:
                self.pressed = False


            screen.blit(self.button1_image, self.button1_pos)
            screen.blit(self.button2_image, self.button2_pos)
            screen.blit(self.button3_image, self.button3_pos)
            screen.blit(self.back_button, self.back_pos)
            screen.blit(self.advance_button, self.advance_pos)
            screen.blit(self.text, (0, 0))

            pygame.display.flip()

    def select_level_menu(self):
        self.play_images = load_image('play2.png', 2, [((x,0),(218, 197))\
                                             for x in range(0, 218, 218)])
        self.play_button = self.advance_images[0]
        self.play_size = self.advance_button.get_size()
        self.play_pos = (710, 500)
        self.level_selected = None
        self.pressed = False
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            self.set_fullscreen()
            screen.blit(self.background, (0, 0))
            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()

            self.level_selected = 1

            if self.play_pos[0] <= mouse_pos[0] <= self.play_pos[0] + self.play_size[0]\
            and self.play_pos[1] <= mouse_pos[1] <= self.play_pos[1] + self.play_size[1]:
                if mouse_press[0]:
                    self.pressed = True
                    main(screen, self.car_selected, self.level_selected)

                if self.pressed and not mouse_press[0]:
                    if self.level_selected is not None:
                        pygame.mixer.music.stop()
                        if main(screen, self.car_selected, self.level_selected) == False:
                            self.main_menu()
            else:
                self.play_button = self.play_images[0]
            if not mouse_press[0]:
                self.pressed = False
            screen.blit(self.back_button, self.back_pos)
            screen.blit(self.play_button, self.play_pos)
            screen.blit(self.text, (0, 0))

            pygame.display.flip()


pygame.init()

screen = pygame.display.set_mode((1024, 768), 0, 32)

pygame.display.set_caption("Test Drive")
menu = Menu()
menu.main_menu()
