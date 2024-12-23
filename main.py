import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(700, 500)


states = pandas.read_csv("50_states.csv")
states_num = len(states)
states_list = states["state"].to_list()
states_x_co = states["x"].to_list()
states_y_co = states["y"].to_list()

correct_guesses = []
game_on = True
while game_on:
    answer_state = screen.textinput(title=f"You guessed: {len(correct_guesses)}/{states_num}", prompt="What's the state's name").title()
    state_row = states[states["state"] == answer_state]
    for state in states_list:
        if answer_state == state:
            if answer_state not in correct_guesses:

                row_index = state_row.index[0]
                x_coordinate = state_row["x"].values[0]
                y_coordinate = state_row["y"].values[0]

                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(x_coordinate, y_coordinate)
                writer.write(answer_state, align="center", font=("Arial", 12, "bold"))
                correct_guesses.append(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if states_num == len(correct_guesses):
        game_on = False
