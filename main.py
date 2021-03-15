import turtle
import pandas as pd
screen= turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725,491)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state=[]
while len(guessed_state)<50:
    answer = screen.textinput(title = "Guess the state",
                              prompt = str(len(guessed_state)) +'/50' + "What's another state name?").title()
    print(answer)
    if answer == 'Exit':
        missing_states=[]
        for state in all_states:
            if state not in guessed_state:
               missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("States to Learn")
        print(missing_states)
        break

    if answer in all_states:
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x) , int(state_data.y))
        t.write(state_data.state.item())

#To get x,y cordinates
# def get_cordinates(x,y):
#     print(x,y)
# turtle.onscreenclick(get_cordinates)
# turtle.mainloop()


screen.exitonclick()