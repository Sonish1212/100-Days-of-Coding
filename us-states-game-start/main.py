import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. State Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tim = turtle.Turtle()
tim.shape('circle')
tim.penup()
tim.hideturtle()

data = pandas.read_csv('50_states.csv')
x_axis = data.x
y_axis = data.y
all_state = data.state.to_list()
score = 0

guessed_state = []


def check_state():

    if answer_state in all_state:
        guessed_state.append(answer_state)
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_state)


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_state)}"/ 50"Give the state name',
                                    prompt='What is the name of another state?').title()
    if answer_state == 'Exit':
        missing_state = [state for state in all_state if state not in guessed_state]
        # for state in all_state:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        state_to_learn = {"state": missing_state}
        write_data = pandas.DataFrame(state_to_learn)
        write_data.to_csv('State to learn')
        break
    check_state()
    score += 1











