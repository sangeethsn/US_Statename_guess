from turtle import Turtle, Screen
import pandas as pd

tur = Turtle()
turtle = Turtle()
turtle.hideturtle()
tur.hideturtle()
num = 0
screen = Screen()
screen.title("U.S State Game")

img = "blank_states_img.gif"
screen.bgpic(img)
state_file = pd.read_csv("50_states.csv")
state_names = state_file["state"]
leng_state_names =state_names.to_list()
already_guessed =[]
not_guessed = []

game_on = True
while game_on:

    answer_state = screen.textinput(title=f"{num}/50Guess the state?", prompt="what is the name of another state?").title()
    if answer_state =="Exit":
        break

    if answer_state in already_guessed:
        tur.penup()
        tur.goto(-70,-20)
        tur.write("This is already guessed!", font=("courier", 20, "normal"))

    if len(already_guessed) == len(leng_state_names)-1:
        game_on = False
        turtle.goto(-70, 0)
        turtle.write("You Won! Congrats", font=("courier", 20, "normal"))

    for state in state_names:
        if answer_state == state and answer_state not in already_guessed:
            tur.clear()
            num += 1
            already_guessed.append(answer_state)
            x = state_file.loc[state_file['state'] == state,'x'].values[0]
            y = state_file.loc[state_file['state'] == state,'y'].values[0]
            turtle.penup()
            turtle.hideturtle()
            turtle.goto(x,y)
            turtle.write(answer_state)
        if state not in already_guessed:
            not_guessed.append(state)

dict = {
    "States":not_guessed
}
df = pd.DataFrame(dict)
save_csv = df.to_csv("Sate_names.csv")