import math
import statistics

def calc_factorial():
    for i in range(1, 17, 5):
        print(f'{i}! = {math.factorial(i)}')

def calc_statistics(st):
    print()
    print(st)
    print(f'중앙 값: {statistics.median(st):.2f}')
    print(f'평균: {statistics.mean(st):.2f}')
    print(f'분산: {statistics.variance(st):.2f}')
    print(f'표준편차: {statistics.stdev(st):.2f}')

if __name__ == '__main__':
    calc_factorial()

    st = [80, 99, 77, 65, 92, 74, 82]
    calc_statistics(st)
