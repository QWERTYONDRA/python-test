import turtle

# create a turtle object
t = turtle.Turtle()

# draw the cat's head
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)

# draw the cat's ears
t.penup()
t.goto(40, 40)
t.pendown()
t.setheading(60)
t.circle(40, 120)
t.penup()
t.goto(-40, 40)
t.pendown()
t.setheading(120)
t.circle(40, 120)

# draw the cat's eyes
t.penup()
t.goto(-30, 0)
t.pendown()
t.dot(20)
t.penup()
t.goto(30, 0)
t.pendown()
t.dot(20)

# draw the cat's nose
t.penup()
t.goto(0, -20)
t.pendown()
t.dot(10)

# draw the cat's mouth
t.penup()
t.goto(-30, -40)
t.pendown()
t.setheading(-30)
t.circle(35, 60)

# hide the turtle
t.hideturtle()

# keep the window open
turtle.done()
