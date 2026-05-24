# ==== IMPORTS ============================================
import pygame
import sys

# Custom imports
from scripts.entities.player import Player
from scripts.core.input_handler import InputHandler
from ui.hud import draw_hud, init_hud
from ui.codex import Editor

# ==== INITIALIZATION ============================================
pygame.init()
pygame.key.set_repeat(400, 30)
init_hud()

# ==== WINDOW SETUP ============================================
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HexRuntime Prototype")

clock = pygame.time.Clock()

# ==== OBJECTS INITIALIZATION ============================================
player = Player(WIDTH // 2, HEIGHT // 2, 50, 5, 100, 100)
input = InputHandler()
codex = Editor()
codex.read_spell()

# ==== MAIN LOOP =============================================
running = True
codex_open = False

while running:
    dt = clock.tick(60)

    # Get all events once
    events = pygame.event.get()

    # Update input handler
    running = input.update(events)

    # Toggle Codex
    if input.toggle_codex:
        codex_open = not codex_open
        codex.active = codex_open
        continue  # Skip the rest of the loop to avoid processing player movement when toggling codex
    
    # Process input
    if codex_open:
        codex.input_handler(events)
    else:
        player.move(input, HEIGHT, WIDTH)

    # Render
    screen.fill((20, 20, 30))
    player.draw_character(screen)
    draw_hud(player, screen)

    if(codex_open):
        codex.update(screen, HEIGHT, WIDTH)
        
    pygame.display.flip()

pygame.quit()
sys.exit()


# # Test command
# keys = pygame.key.get_pressed()

# if keys[pygame.K_SPACE]:
#     player.health -= 1
#     if player.health < 0:
#         player.health = 0

# if not keys[pygame.K_SPACE]:
#     player.health += 0.5
#     if player.health > player.max_health:
#         player.health = player.max_health