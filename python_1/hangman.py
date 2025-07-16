#Turtle lets me draw graphics by controlling the turtle and the random picks a random word for the game
import turtle
import random

#Setup of the screen and turtle
screen = turtle.Screen()
screen.title("Hangman Game")
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

#Word bank and the game's variables
word_list = ["python", "turtle", "code", "drawing"]
chosen_word = random.choice(word_list)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

#Definition of the drawing of the gallow; the visual stage
def draw_gallows():
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

#Definitions for the body parts being drawn one by one for every wrong guess
def draw_head():
    pen.penup()
    pen.goto(100, 100)
    pen.setheading(0)
    pen.pendown()
    pen.circle(25)

def draw_body():
    pen.penup()
    pen.goto(100, 100)
    pen.setheading(270)
    pen.pendown()
    pen.forward(75)

def draw_left_arm():
    pen.penup()
    pen.goto(100, 75)
    pen.setheading(220)
    pen.pendown()
    pen.forward(50)

def draw_right_arm():
    pen.penup()
    pen.goto(100, 75)
    pen.setheading(-40)
    pen.pendown()
    pen.forward(50)

def draw_left_leg():
    pen.penup()
    pen.goto(100, 25)
    pen.setheading(240)
    pen.pendown()
    pen.forward(50)

def draw_right_leg():
    pen.penup()
    pen.goto(100, 25)
    pen.setheading(-60)
    pen.pendown()
    pen.forward(50)

# Definition of The stage controller
def draw_stage(stage):
    stages = [draw_head, draw_body, draw_left_arm, draw_right_arm, draw_left_leg, draw_right_leg]
    if stage < len(stages):
        stages[stage]()

#Shows the state of the word, helps the player keep track of their progress

def display_word():
    display = ""
    for letter in chosen_word:
        display += letter if letter in guessed_letters else "_"
        display += " "
    print(display)

# GAME CODE - START

#Turtle draws the gallows before user starts playing
draw_gallows()

    #Ensures the loop continues long as the number of wrong guesses is under 6 (the max number of guesses) and the user hasn't guessed all the letters in the word.
while wrong_guesses < max_wrong and set(guessed_letters) != set(chosen_word):

    #Prints the underscores for the letters and letters guessed
    display_word() 
    guess = screen.textinput("Your Guess", "Guess a letter:").lower()

    if not guess or not guess.isalpha() or len(guess) != 1:
        print("Please enter one valid letter.")
        continue
    #Makes sure the input works
    if guess in guessed_letters:
        print("You already guessed that.")
        continue
    #Checks if the guess has already been guessed
    guessed_letters.append(guess)
   
    #Shows a message if the guess is wrong or right
    if guess not in chosen_word:
        draw_stage(wrong_guesses)
        wrong_guesses += 1
        print(f"Wrong! {max_wrong - wrong_guesses} tries left.")
    else:
        print("Good guess!")


#Ending message
if set(chosen_word) == set(guessed_letters):
    display_word()
    print("\nYou guessed the word!")  # ← Your custom message
    print(f"The word was: {chosen_word}")
else:
    print("\nGame Over.")
    print(f"The word was: {chosen_word}")
