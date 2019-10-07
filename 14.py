#
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
#
# Hint: The basic equation of a circle is x2 + y2 = r2.
import random
def estimate(x):
    circle_points = 0
    square_points = 0
    for i in range(0,x):
        x = random.random()
        y = random.random()
        d = pow(x, 2) + pow(y, 2)
        if d <= 1:
            circle_points += 1
        square_points += 1
    pi = 4*(circle_points/square_points)
    pi = round(pi,3)
    return pi
print(estimate(1000000))
