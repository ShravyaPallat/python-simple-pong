import turtle as t

# Set up the screen
window = t.Screen()
window.title("Pong Game")
window.bgcolor("white")
window.setup(width=1000, height=600)
window.tracer(0)

# Score variables
left_player = 0
right_player = 0

# Left paddle
left_pad = t.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# Right paddle
right_pad = t.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Ball
hit_ball = t.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 0.15
hit_ball.dy = -0.15

# Pen (Scoreboard)
pen = t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Left Player: 0  Right Player: 0", align="center", font=("Courier", 24, "normal"))

# Functions to move paddles
def paddleaup():
    y = left_pad.ycor()
    if y < 250:  # Keep paddle within bounds
        y += 20
    left_pad.sety(y)

def paddleadown():
    y = left_pad.ycor()
    if y > -240:  # Keep paddle within bounds
        y -= 20
    left_pad.sety(y)

def paddlebup():
    y = right_pad.ycor()
    if y < 250:  # Keep paddle within bounds
        y += 20
    right_pad.sety(y)

def paddlebdown():
    y = right_pad.ycor()
    if y > -240:  # Keep paddle within bounds
        y -= 20
    right_pad.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(paddleaup, "e")
window.onkeypress(paddleadown, "x")
window.onkeypress(paddlebup, "Up")
window.onkeypress(paddlebdown, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Border checking
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1
        left_player += 1
        pen.clear()
        pen.write(f"Left Player: {left_player}  Right Player: {right_player}", align="center", font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1
        right_player += 1
        pen.clear()
        pen.write(f"Left Player: {left_player}  Right Player: {right_player}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (360 < hit_ball.xcor() < 370) and (right_pad.ycor() - 50 < hit_ball.ycor() < right_pad.ycor() + 50):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (-370 < hit_ball.xcor() < -360) and (left_pad.ycor() - 50 < hit_ball.ycor() < left_pad.ycor() + 50):
        hit_ball.setx(-360)
        hit_ball.dx *= -1
