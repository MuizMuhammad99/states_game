import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
turtle.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

#def get_coordinates_mouse_click(x,y):
 #   print(x,y)

#turtle.onscreenclick(get_coordinates_mouse_click)
#turtle.mainloop()

answer_states = []
data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()

while len(answer_states) < 50:
    answer = screen.textinput(title=f"{len(answer_states)}/50 states", prompt="Can you name a US State?").title()

    if answer in data_list:
        if answer not in answer_states:
            answer_states.append(answer)
        state_data = data[data.state == answer]
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(answer)

screen.exitonclick()