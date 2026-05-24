import pygame

class Player():
    def __init__(self, x, y, size, speed, max_health, max_mana):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.max_health = max_health
        self.health = max_health
        self.max_mana = max_mana
        self.mana = max_mana
        
        
    def draw_character(self, screen):
        pygame.draw.rect(
            screen,
            (120, 80, 255),
            (self.x, self.y, self.size, self.size)
        )
        
        
    def move(self, input_handler, height_limit, width_limit):
        if input_handler.move_up:
            self.y -= self.speed
            if self.y < 0:
                self.y = 0

        if input_handler.move_down:
            self.y += self.speed
            if self.y > height_limit - self.size:
                self.y = height_limit - self.size

        if input_handler.move_left:
            self.x -= self.speed
            if self.x < 0:
                self.x = 0

        if input_handler.move_right:
            self.x += self.speed
            if self.x > width_limit - self.size:
                self.x = width_limit - self.size
        
        
    