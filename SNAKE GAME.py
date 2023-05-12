from turtle import Turtle, Screen
from  snake import Snake
import time
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #DETECT COLLISION WIH FOOD
    if snake.head.distance(food) < 30:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # DETECT COLLISION WIH WALL
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()



    # DETECT COLLUSION WINT TAIL
    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()