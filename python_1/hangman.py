# Turtle Hangman Game
import turtle
import random

# Setup
screen = turtle.Screen()
screen.title("Hangman Game")
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Game variables
word_list = ["python", "turtle", "code", "drawing"]
chosen_word = random.choice(word_list)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Drawing functions
def draw_gallows():
    """Draws the base structure (gallows) where the hangman appears."""
    pen.penup()
    pen.goto(-100, -150)
    pen.pendown()
    pen.forward(200)
    pen.backward(100)
    pen.left(90)
    pen.forward(250)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(50)

def draw_head():
    """Draws the head of the hangman."""
    pen.penup()
    pen.goto(100, 100)
    pen.setheading(0)
    pen.pendown()
    pen.circle(25)

def draw_body():
    """Draws the body of the hangman."""
    pen.penup()
    pen.goto(100, 100)
    pen.setheading(270)
    pen.pendown()
    pen.forward(75)

def draw_left_arm():
    """Draws the left arm of the hangman."""
    pen.penup()
    pen.goto(100, 75)
    pen.setheading(220)
    pen.pendown()
    pen.forward(50)

def draw_right_arm():
    """Draws the right arm of the hangman."""
    pen.penup()
    pen.goto(100, 75)
    pen.setheading(-40)
    pen.pendown()
    pen.forward(50)

def draw_left_leg():
    """Draws the left leg of the hangman."""
    pen.penup()
    pen.goto(100, 25)
    pen.setheading(240)
    pen.pendown()
    pen.forward(50)

def draw_right_leg():
    """Draws the right leg of the hangman."""
    pen.penup()
    pen.goto(100, 25)
    pen.setheading(-60)
    pen.pendown()
    pen.forward(50)

def draw_stage(stage):
    """Chooses which body part to draw based on the number of wrong guesses."""
    stages = [draw_head, draw_body, draw_left_arm, draw_right_arm, draw_left_leg, draw_right_leg]
    if stage < len(stages):
        stages[stage]()

def display_word():
    """Shows the current state of the guessed word, with letters and blanks."""
    display = ""
    for letter in chosen_word:
        display += letter if letter in guessed_letters else "_"
        display += " "
    print(display)

# Run game
draw_gallows()

while wrong_guesses < max_wrong and not all(letter in guessed_letters for letter in chosen_word):
    display_word()
    guess = screen.textinput("Your Guess", "Guess a letter:").lower()

    if not guess or not guess.isalpha() or len(guess) != 1:
        print("Please enter one valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that.")
        continue

    guessed_letters.append(guess)

    if guess not in chosen_word:
        draw_stage(wrong_guesses)
        wrong_guesses += 1
        print(f"Wrong! {max_wrong - wrong_guesses} tries left.")
    else:
        print("Good guess!")

if all(letter in guessed_letters for letter in chosen_word):
    display_word()
    print("\nYou guessed the word!")
    print(f"The word was: {chosen_word}")
else:
    print("\nGame Over.")
    print(f"The word was: {chosen_word}")