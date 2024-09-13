import pygame
import sys

# Initialize pygame
pygame.init()

# Set up screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mystery of the Enchanted Forest')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define fonts
font = pygame.font.SysFont(None, 36)

# Global variables for game state
current_scene = "intro"

# Function to render text on the screen
def render_text(text, pos, color=BLACK):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (pos[0], pos[1] + i * 40))

# Function to handle scenes
def handle_scene(scene):
    screen.fill(WHITE)
    if scene == "intro":
        render_text("You are at the entrance of a dark forest.\nThe forest is said to be enchanted.", (50, 50))
        render_text("Do you want to enter?", (50, 200))
        render_text("1. Yes", (50, 250))
        render_text("2. No, stay outside", (50, 300))

    elif scene == "enter_forest":
        render_text("You enter the forest. The air is cold, and shadows move.", (50, 50))
        render_text("You see a cabin to the left and a glowing tree to the right.", (50, 200))
        render_text("1. Go to the cabin", (50, 250))
        render_text("2. Approach the glowing tree", (50, 300))

    elif scene == "stay_outside":
        render_text("You decide to stay outside.\nA mysterious figure appears and hands you a map.", (50, 50))
        render_text("Do you take the map?", (50, 200))
        render_text("1. Yes", (50, 250))
        render_text("2. No", (50, 300))

    elif scene == "go_to_cabin":
        render_text("You walk to the cabin and knock on the door.\nAn old woman opens it.", (50, 50))
        render_text("\"Welcome, traveler. I have been expecting you,\" she says.\nDo you enter?", (50, 200))
        render_text("1. Yes", (50, 250))
        render_text("2. No", (50, 300))

    elif scene == "glowing_tree":
        render_text("You approach the glowing tree and touch it.\nSuddenly, you are transported to another dimension!", (50, 50))
        render_text("Do you explore the new dimension?", (50, 200))
        render_text("1. Yes", (50, 250))
        render_text("2. No", (50, 300))

    elif scene == "take_map":
        render_text("You take the map and follow it.\nIt leads you to a hidden cave.", (50, 50))
        render_text("Do you enter the cave?", (50, 200))
        render_text("1. Yes", (50, 250))
        render_text("2. No", (50, 300))

    elif scene == "no_map":
        render_text("You refuse the map and walk away.\nSuddenly, the figure vanishes into thin air.", (50, 50))
        render_text("Without direction, you wander lost.", (50, 200))
        render_text("Game Over!", (50, 300))
        render_text("Press Space to Restart", (50, 400))

    elif scene == "enter_cabin":
        render_text("You enter the cabin and find an ancient book.\nThe old woman asks if you want to read it.", (50, 50))
        render_text("1. Yes", (50, 250))
        render_text("2. No", (50, 300))

    elif scene == "explore_dimension":
        render_text("You explore the new dimension and discover a kingdom.\nDo you seek out the ruler?", (50, 50))
        render_text("1. Yes", (50, 250))
        render_text("2. No", (50, 300))

    elif scene == "cave_ending":
        render_text("You enter the cave and find a treasure chest!\nYou have uncovered the hidden treasure!", (50, 50))
        render_text("Congratulations, you win!", (50, 200))
        render_text("Press Space to Restart", (50, 300))

    elif scene == "game_over":
        render_text("Game Over!", (50, 200))
        render_text("Press Space to Restart", (50, 300))

    pygame.display.update()

# Main game loop
def game_loop():
    global current_scene
    running = True

    while running:
        handle_scene(current_scene)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if current_scene == "intro":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        current_scene = "enter_forest"
                    elif event.key == pygame.K_2:
                        current_scene = "stay_outside"
            
            elif current_scene == "enter_forest":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        current_scene = "go_to_cabin"
                    elif event.key == pygame.K_2:
                        current_scene = "glowing_tree"

            elif current_scene == "stay_outside":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        current_scene = "take_map"
                    elif event.key == pygame.K_2:
                        current_scene = "no_map"

            elif current_scene == "go_to_cabin":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        current_scene = "enter_cabin"
                    elif event.key == pygame.K_2:
                        current_scene = "game_over"

            elif current_scene == "glowing_tree":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        current_scene = "explore_dimension"
                    elif event.key == pygame.K_2:
                        current_scene = "game_over"

            elif current_scene == "take_map":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        current_scene = "cave_ending"
                    elif event.key == pygame.K_2:
                        current_scene = "game_over"

            elif current_scene == "no_map":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    current_scene = "intro"

            elif current_scene == "enter_cabin":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        current_scene = "cave_ending"  # Reading the book leads to hidden treasure
                    elif event.key == pygame.K_2:
                        current_scene = "game_over"

            elif current_scene == "explore_dimension":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        current_scene = "cave_ending"
                    elif event.key == pygame.K_2:
                        current_scene = "game_over"

            elif current_scene in ["game_over", "cave_ending"]:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    current_scene = "intro"

        pygame.display.update()

# Run the game loop
game_loop()
