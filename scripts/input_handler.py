import pygame

class InputHandler():
    def __init__(self):
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        
    def update(self):
        keys = pygame.key.get_pressed()
        
        self.move_up = keys[pygame.K_w]
        self.move_down = keys[pygame.K_s]
        self.move_left = keys[pygame.K_a]
        self.move_right = keys[pygame.K_d]