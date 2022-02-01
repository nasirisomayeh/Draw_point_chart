
from turtle import dot
import numpy as np
import matplotlib.pyplot as plt

dots_x =[]
dots_y =[]

while True :
    user_input= input('Enter x and y:')
    if user_input == 'exit':
        break
    x , y = user_input.split(',')

    dots_x.append(int(x))
    dots_y.append(int(y))

    plt.scatter(dots_x , dots_y , alpha = 0.5)
    plt.title('nasirisomayeh2@gmail.com')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()
