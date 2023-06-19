import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Load hangman images
hangman_images = []
for i in range(7):
    image = pygame.image.load(f"hangman{i}.png")
    hangman_images.append(image)

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up fonts
font_title = pygame.font.SysFont("Arial", 50, True)
font_word = pygame.font.SysFont("Arial", 60)
font_result = pygame.font.SysFont("Arial", 80)
font_hint = pygame.font.SysFont("Arial", 30)

# Load words from file
with open("words.txt", "r") as file:
    words = file.readlines()

# Select a random word
word = random.choice(words).strip().upper()
hint = "This is a hint for the word."

# Initialize game variables
hangman_status = 0
guessed_letters = []
correct_letters = []

# Set up game loop
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(WHITE)

    # Draw title
    title_text = font_title.render("Hangman Game", True, BLACK)
    win.blit(title_text, (WIDTH / 2 - title_text.get_width() / 2, 20))

    # Draw hint
    hint_text = font_hint.render(hint, True, BLACK)
    win.blit(hint_text, (WIDTH / 2 - hint_text.get_width() / 2, 100))

    # Draw word
    display_word = ""
    for letter in word:
        if letter in correct_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    word_text = font_word.render(display_word, True, BLACK)
    win.blit(word_text, (WIDTH / 2 - word_text.get_width() / 2, 400))

    # Draw hangman image
    win.blit(hangman_images[hangman_status], (WIDTH / 2 - hangman_images[hangman_status].get_width() / 2, 150))

    # Draw guessed letters
    guessed_text = font_hint.render("Guessed Letters: " + " ".join(guessed_letters), True, BLACK)
    win.blit(guessed_text, (WIDTH / 2 - guessed_text.get_width() / 2, 500))

    pygame.display.update()


def display_result(result):
    pygame.time.delay(1000)
    win.fill(WHITE)
    result_text = font_result.render(result, True, RED)
    win.blit(result_text, (WIDTH / 2 - result_text.get_width() / 2, HEIGHT / 2 - result_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                letter = chr(event.key).upper()
                if letter not in guessed_letters:
                    guessed_letters.append(letter)
                    if letter in word:
                        correct_letters.append(letter)
                    else:
                        hangman_status += 1

    draw()

    # Check if the game is over
    won = True
    for letter in word:
        if letter not in correct_letters:
            won = False
            break

    if won:
        display_result("You won!")
        break
    elif hangman_status == 6:
        display_result("You lost!")
        break

pygame.quit()
