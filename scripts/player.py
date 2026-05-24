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
        
        self.font = pygame.font.SysFont("Arial", 20)
        
        
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
        
        
    def draw_hud(self, screen):
        # Health text
        text = self.font.render(f"Health: {int(self.health)}/{self.max_health}", True, (255, 255, 255))
        screen.blit(text, (20, 0))
        
        # Missing health bar background
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (20, 20, self.max_health * 2, 20)
        )
        
        # Current health bar
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (20, 20, self.health * 2, 20)
        )
        
        # Mana text
        text = self.font.render(f"Mana: {int(self.mana)}/{self.max_mana}", True, (255, 255, 255))
        screen.blit(text, (20, 40))
        
        # Missing mana bar background
        pygame.draw.rect(
            screen,
            (0, 0, 255),
            (20, 60, self.max_mana * 2, 20)
        )
        
        # Current mana bar
        pygame.draw.rect(
            screen,
            (0, 255, 255),
            (20, 60, self.mana * 2, 20)
        )
    