import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hangman Game")

# Load hangman images
hangman_images = []
for i in range(7):
    hangman_img = pygame.image.load(f"hangman{i}.png").convert_alpha()
    hangman_images.append(hangman_img)

# Load words and hints from file
with open("words.txt", "r") as file:
    word_list = file.readlines()

# Select a random word from the list
word_hint = random.choice(word_list).strip().split(": ")
word = word_hint[0]
hint = word_hint[1]

# Create a list to store guessed letters
guessed_letters = []

# Set up the game loop
running = True
current_image = 0
game_over = False
game_won = False

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_over and not game_won:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key).upper()
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                        if letter not in word:
                            current_image += 1

    # Draw the hangman image
    screen.blit(hangman_images[current_image], (screen_width / 2 - 150, screen_height / 2 - 200))

    # Draw the word with blanks and correctly guessed letters
    display_word = ""
    for char in word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "
    font = pygame.font.Font(None, 36)
    text = font.render(display_word, True, BLACK)
    text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(text, text_rect)

    # Draw the hint
    hint_font = pygame.font.Font(None, 24)
    hint_text = hint_font.render("Hint: " + hint, True, BLACK)
    hint_rect = hint_text.get_rect(center=(screen_width / 2, screen_height / 2 + 100))
    screen.blit(hint_text, hint_rect)

    # Check if the game is over or won
    if current_image == 6:
        game_over = True
    if all(char in guessed_letters for char in word):
        game_won = True

    # Display game over or win messages
    if game_over:
        game_over_font = pygame.font.Font(None, 72)
        game_over_text = game_over_font.render("Game Over", True, BLACK)
        game_over_rect = game_over_text.get_rect(center=(screen_width / 2, screen_height / 2 + 200))
        screen.blit(game_over_text, game_over_rect)
        word_font = pygame.font.Font(None, 36)
        word_text = word_font.render("The word was: " + word, True, BLACK)
        word_rect = word_text.get_rect(center=(screen_width / 2, screen_height / 2 + 250))
        screen.blit(word_text, word_rect)
        continue_font = pygame.font.Font(None, 24)
        continue_text = continue_font.render("Do you want to continue? (Y/N)", True, BLACK)
        continue_rect = continue_text.get_rect(center=(screen_width / 2, screen_height / 2 + 300))
        screen.blit(continue_text, continue_rect)
        pygame.display.flip()

        response_received = False
        while not response_received:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        response_received = True
                        # Reset the game for a new round
                        current_image = 0
                        game_over = False
                        game_won = False
                        guessed_letters = []
                        word_hint = random.choice(word_list).strip().split(": ")
                        word = word_hint[0]
                        hint = word_hint[1]
                    elif event.key == pygame.K_n:
                        response_received = True
                        running = False

    elif game_won:
        game_won_font = pygame.font.Font(None, 72)
        game_won_text = game_won_font.render("You Win!", True, BLACK)
        game_won_rect = game_won_text.get_rect(center=(screen_width / 2, screen_height / 2 + 200))
        screen.blit(game_won_text, game_won_rect)
        continue_font = pygame.font.Font(None, 24)
        continue_text = continue_font.render("Do you want to continue? (Y/N)", True, BLACK)
        continue_rect = continue_text.get_rect(center=(screen_width / 2, screen_height / 2 + 250))
        screen.blit(continue_text, continue_rect)
        pygame.display.flip()

        response_received = False
        while not response_received:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        response_received = True
                        # Reset the game for a new round
                        current_image = 0
                        game_over = False
                        game_won = False
                        guessed_letters = []
                        word_hint = random.choice(word_list).strip().split(": ")
                        word = word_hint[0]
                        hint = word_hint[1]
                    elif event.key == pygame.K_n:
                        response_received = True
                        running = False

    pygame.display.flip()

# Quit the game
pygame.quit()
