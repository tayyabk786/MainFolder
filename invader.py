import pygame
import sys

# Initialize Pygame
pygame.init()

# Initialize Pygame mixer
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 800, 600
MENU_FONT = pygame.font.SysFont("comicsansms", 75)
MENU_TITLE_FONT = pygame.font.SysFont("comicsansms", 50)
MENU_NAME_FONT = pygame.font.SysFont("comicsansms", 40)
GREEN = (7, 189, 32)
BACKGROUND = pygame.image.load("images/menupic.jpg")
GRAY = (169, 169, 169)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Main Menu")

# Define the main menu options
menu_options = ["Start Game", "Settings", "Exit"]
selected_option = None

# Load and play the soundtrack
pygame.mixer.music.load('Sounds/music.mp3')  # Replace with your soundtrack file
pygame.mixer.music.set_volume(0.5)  # Set the initial volume
pygame.mixer.music.play(-1)  # Loop indefinitely

# Volume control step (adjust as needed)
volume_step = 0.1

def draw_menu():
    screen.fill(BACKGROUND)
    title_text = MENU_TITLE_FONT.render("ALIEN INVADERS", True, GREEN)
    title_name = MENU_NAME_FONT.render("By Hamza & Tayyab", True, GREEN)
     
    screen.blit(title_text, (WIDTH // 5 - title_text.get_width() // 100, 17))
    screen.blit(title_name, (WIDTH // 4 - title_name.get_width() // 600, 90))

    for i, option in enumerate(menu_options):
        text = MENU_FONT.render(option, True, GREEN if selected_option == i else GRAY)
        text_rect = text.get_rect(center=(WIDTH // 2, 250 + i * 100))
        screen.blit(text, text_rect)

def main_menu():
    global selected_option
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                for i, option in enumerate(menu_options):
                    text_rect = MENU_FONT.render(option, True, GREEN).get_rect(center=(WIDTH // 2, 300 + i * 60))
                    if text_rect.collidepoint(mouse_x, mouse_y):
                        selected_option = i
                        break
                else:
                    selected_option = None
            if event.type == pygame.MOUSEBUTTONDOWN and selected_option is not None:
                if selected_option == 0:
                    # Start the game (replace with your game code)
                    print("Starting the game")
                elif selected_option == 1:
                    # Open settings
                    settings_menu()
                elif selected_option == 2:
                    pygame.quit()

        draw_menu()
        pygame.display.flip()

def settings_menu():
    global volume
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pygame.mixer.music.set_volume(min(1.0, pygame.mixer.music.get_volume() + volume_step))
                elif event.key == pygame.K_DOWN:
                    pygame.mixer.music.set_volume(max(0.0, pygame.mixer.music.get_volume() - volume_step))
                elif event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BACKGROUND)
        title_text = MENU_TITLE_FONT.render("Settings", True, GREEN)
        volume_text = MENU_FONT.render(f"Volume: {int(pygame.mixer.music.get_volume() * 100)}%", True, GREEN)
        
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        screen.blit(volume_text, (WIDTH // 2 - volume_text.get_width() // 2, 250))
        
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
