import pygame

label_font = None

def init_hud():
    global label_font
    label_font = pygame.font.SysFont("Arial", 20)

def draw_hud(player,screen):
    # Health text
    text = label_font.render(f"Health: {int(player.health)}/{player.max_health}", True, (255, 255, 255))
    screen.blit(text, (20, 0))
    
    # Missing health bar background
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (20, 20, player.max_health * 2, 20)
    )
    
    # Current health bar
    pygame.draw.rect(
        screen,
        (0, 255, 0),
        (20, 20, player.health * 2, 20)
    )
    
    # Mana text
    text = label_font.render(f"Mana: {int(player.mana)}/{player.max_mana}", True, (255, 255, 255))
    screen.blit(text, (20, 40))
    
    # Missing mana bar background
    pygame.draw.rect(
        screen,
        (0, 0, 255),
        (20, 60, player.max_mana * 2, 20)
    )
    
    # Current mana bar
    pygame.draw.rect(
        screen,
        (0, 255, 255),
        (20, 60, player.mana * 2, 20)
    )