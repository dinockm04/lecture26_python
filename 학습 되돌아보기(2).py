import math
import random

def getarea(r):
    return math.pi * r * r

radius = random.random() * 100

radius = round(radius, 2)
area = round(getarea(radius), 2)

print('원의 반지름 :', radius)
print('원주율 pi :', math.pi)
print(f'반지름 {radius}인 원의 면적은 {area}')
