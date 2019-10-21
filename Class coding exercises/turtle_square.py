import turtle

tortuga = turtle.Turtle()

for i in range(20):
  if i!=0:
    tortuga.penup()
    tortuga.forward(2)
    tortuga.right(90)
    tortuga.forward(2)
    tortuga.left(90)
    tortuga.pendown()

  tortuga.forward(50)
  tortuga.right(90)     # Rotate clockwise by 90 degrees

  tortuga.forward(50)
  tortuga.right(90)

  tortuga.forward(50)
  tortuga.right(90)

  tortuga.forward(50)
  tortuga.right(90)

turtle.done()
