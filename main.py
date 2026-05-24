import pygame
import sys
from scripts.player import Player
from scripts.input_handler import InputHandler

# Inicialização
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HexRuntime Prototype")

clock = pygame.time.Clock()

# Player
player = Player(WIDTH // 2, HEIGHT // 2, 50, 5, 100, 100)

# Input Handler
input = InputHandler()

# Loop principal
running = True
while running:
    dt = clock.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Inputs
    input.update()
    player.move(input, HEIGHT, WIDTH)


    # Test command
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        player.health -= 1
        if player.health < 0:
            player.health = 0
    
    if not keys[pygame.K_SPACE]:
        player.health += 0.5
        if player.health > player.max_health:
            player.health = player.max_health


    # Render
    screen.fill((20, 20, 30))

    player.draw_character(screen)
    player.draw_hud(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()