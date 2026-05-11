class Car:
    def __init__(self, company, year, color):
        self.company = company
        self.year = year
        self.color = color

    def __str__(self):
        return f'자동차 회사: {self.company}, 년식: {self.year}, 색상: {self.color}'

    def __eq__(self, other):
        return self.company == other.company and self.year == other.year and self.color == other.color


mycar = Car('현대', 2020, '검정')
yourcar = Car('기아', 2021, '백색')

print(mycar)
print(yourcar)
print(mycar == yourcar)
