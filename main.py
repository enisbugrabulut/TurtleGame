import turtle
import random

window = turtle.Screen()
window.bgcolor("light blue")
window.setup(width=800, height=600)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window.title("Catch the Turtle")

FONT = ('Arial', 30, 'normal')

turtle1 = turtle.Turtle(shape="turtle")
turtle1.shapesize(3)
turtle1.color("green")

timer_turtle = turtle.Turtle(visible=False)
timer_turtle.teleport(0, 250)

score_turtle = turtle.Turtle(visible=False)
score_turtle.teleport(0, 220)

final_turtle = turtle.Turtle(visible=False)

score = 0

def spawn_turtle():
    turtle1.hideturtle()
    turtle1.teleport(random.randint(int(-window.window_width() / 2 + 50), int(window.window_width() / 2 - 50)),
                     random.randint(int(-window.window_height() / 2 + 50), int(window.window_height()/ 2 - 150)))
    turtle1.showturtle()
    turtle1.onclick(increase_score)
    print(turtle1.position())

def countdowner(game_time):
    timer_turtle.clear()
    score_turtle.clear()
    if game_time > 0:
        timer_turtle.write(f"Time left: {game_time}", align='center', font=FONT)
        score_turtle.write(f"Your score: {score}", align='center', font=FONT)
        spawn_turtle()
        window.ontimer(lambda: countdowner(game_time - 1), 1000)
    else:
        timer_turtle.write(f"Time left: {game_time}", align='center', font=FONT)
        score_turtle.write(f"Your score: {score}", align='center', font=FONT)
        final_turtle.write(f"Congratulations! Your score: {score}", align='center', font=FONT)
        window.exitonclick()

def increase_score(x,y):
    global score
    score += 1

if __name__ == "__main__":
    countdowner(5)
    window.mainloop()