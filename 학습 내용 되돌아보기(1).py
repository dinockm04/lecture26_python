# 01

class TV:
    def __init__(self, size):
        self.size = size


class Car:
    def __init__(self, color):
        self.color = color


# 02

class TV:
    cnt_products = 0

    def __init__(self, size):
        self.size = size
        TV.cnt_products += 1


mine = TV(60)

print(TV.cnt_products)
