import turtle

first_turtle= turtle.Turtle();
first_turtle.speed(1000)


def square():  
 
  first_turtle.forward(100)
  first_turtle.right(90)
  first_turtle.forward(100)
  first_turtle.right(90)
  first_turtle.forward(100)
  first_turtle.right(90)
  first_turtle.forward(100)


second_turtle = turtle.Turtle();
second_turtle.speed(100)
def rectangle():
  second_turtle.forward(50)
  second_turtle.left(45)
  second_turtle.forward(50)
  second_turtle.left(45)
  second_turtle.forward(50)
  second_turtle.left(45)
  second_turtle.forward(50)
  second_turtle.left(45)
  second_turtle.forward(50)
  second_turtle.left(45)
  second_turtle.forward(50)
  second_turtle.left(45)
  second_turtle.forward(50)
  second_turtle.left(45)
  second_turtle.forward(50)

 
#square()
#first_turtle.forward(300)
#square()

elephent_weight = 2000
ant_weight = 0.1

#if elephent_weight < ant_weight :
#  square()
#else:
#  first_turtle.forward(20)

#uzair = "happy"
#while uzair == "happy":
#  first_turtle.forward(10)

for count in range(4):
  square()

for count in range(8):
 rectangle()



