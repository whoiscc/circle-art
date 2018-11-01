#!/usr/bin/env python3
# usage: cadraw [radius] [circle list]
import sys
import turtle
from fractions import Fraction
import math
import random


arg_radius = eval(sys.argv[1])
arg_circle_list = eval(sys.argv[2])

arg_preview = False
arg_scale = True
for arg in sys.argv[3:]:
    if arg == '--preview':
        arg_preview = True
    elif arg == '--no-scale':
        arg_scale = False
    else:
        raise Exception(f'wrong argument: {arg}')

circle_list = [(t, Fraction(Fraction(n), Fraction(d))) for t, n, d in arg_circle_list]
print(f'radius: {arg_radius} circles: {circle_list}')


def cal_r2(r1, k):
    return 2 * r1 * math.sin(0.5 * k * math.pi)


def cal_beta(k):
    return 0.5 * (1 - float(k)) * math.pi


def cal_gamma(k):
    return float(k) * math.pi


def draw(r1, r2, k, inner=True):
    beta = cal_beta(k)
    gamma = cal_gamma(k)
    for _i in range((1 / (k / 2)).numerator):
        turtle.pendown()
        turtle.right(beta)
        if inner:
            turtle.circle(-r2, 2 * beta)
        else:
            turtle.circle(-r2, -2 * (math.pi - beta))
        turtle.penup()
        turtle.right(beta)
        turtle.circle(-r1, gamma)


def scale(r):
    size = min(turtle.window_width(), turtle.window_height())
    ratio = 0.5 * 1.05 * (r * 2 / size)
    width = turtle.window_width()
    height = turtle.window_height()
    turtle.setworldcoordinates(
        -ratio * width, -ratio * height, ratio * width, ratio * height)


turtle.radians()
if arg_scale:
    scale(arg_radius)
if arg_preview:
    turtle.speed(0)

base_radius = arg_radius

turtle.penup()
turtle.left(math.pi)
turtle.forward(base_radius)
turtle.right(0.5 * math.pi)
turtle.pendown()
turtle.circle(-base_radius)
turtle.penup()
turtle.home()
turtle.left(0.5 * math.pi)

inner_r1 = outer_r1 = arg_radius
previous_r1 = 0
for i, (t, k) in enumerate(circle_list):
    if t == 'i':
        inner = True
        r1 = inner_r1
    elif t == 'o':
        inner = False
        r1 = outer_r1
    else:
        raise Exception(f'wrong circle type: {t}')

    turtle.penup()
    turtle.left(0.5 * math.pi)
    turtle.forward(r1 - previous_r1)
    turtle.right(0.5 * math.pi)
    turtle.circle(-r1, random.random() * math.tau)
    turtle.pendown()

    r2 = cal_r2(r1, k)
    if arg_scale:
        if inner:
            scale(r1)
        else:
            scale(r1 + r2)
    draw(r1, r2, k, inner=inner)
    if inner:
        inner_r1 = abs(r1 - r2)
    else:
        outer_r1 = r1 + r2
    previous_r1 = r1

turtle.penup()
turtle.home()
turtle.hideturtle()

scale(outer_r1)

turtle.done()
