# input_handler.py

import pygame

class InputHandler:

    def __init__(self):
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        self.interact = False

        self.toggle_codex = False


    def update(self, events):
        # Reset one-frame actions
        self.toggle_codex = False

        # Continuous input
        keys = pygame.key.get_pressed()

        # Moviment
        self.move_up = keys[pygame.K_w]
        self.move_down = keys[pygame.K_s]
        self.move_left = keys[pygame.K_a]
        self.move_right = keys[pygame.K_d]

        self.interact = keys[pygame.K_e]

        # Events
        for event in events:
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                # Open codex
                if event.key == pygame.K_TAB:
                    self.toggle_codex = True
                    
                # Quit
                if event.key == pygame.K_ESCAPE:
                    return False

        return True