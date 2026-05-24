import pygame

class Editor():
    def __init__(self):
        self.active = False
        self.spell_text = ""
        self.font_size = 24
        self.font = pygame.font.SysFont("Arial", self.font_size)
    
    
    def read_spell(self, spell_name="current_spell.txt"):
        with open(f"spells/{spell_name}", "r") as f:
            self.spell_text = f.read()
    
    
    def _render_text(self, screen, height, width):
        # Split the text into lines and render each line separately
        splited_text = self.spell_text.split("\n")
        for i, line in enumerate(splited_text):
            # Render the line and blit it to the screen
            text_surface = self.font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (width // 2 + 20, 20 + i * (self.font_size + 5)))
    
    
    def update(self, screen, height, width):
        if self.active:
            # Draw a simple overlay for the codex
            overlay = pygame.Surface((width // 2, height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))  # Semi-transparent black
            screen.blit(overlay, (width // 2, 0))

            # Draw codex content
            self._render_text(screen, height, width)
            
    
    def input_handler(self, events):
        if self.active:
            for event in events:
                # Special keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.spell_text = self.spell_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        self.spell_text += "\n"

                # Normal text 
                if event.type == pygame.TEXTINPUT:
                    self.spell_text += event.text
    

# text = label_font.render(f"Mana: {int(player.mana)}/{player.max_mana}", True, (255, 255, 255))
# screen.blit(text, (20, 40))