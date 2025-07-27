# At first, use 'turtle'.(essential package)
import turtle

# Define 's' as variable with type 'screen'
s = turtle.Screen()

# Define speed of draw equals 3.
turtle.speed(3)

# Define for loop that include 30 circles with different Radius with one central point.
for i in range(30):
    turtle.circle(5*i)
turtle.done()