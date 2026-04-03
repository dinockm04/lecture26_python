# index 찾기
def getIndex(num_list, target):
    if target in num_list:
        return num_list.index(target)
    else:
        return -1


# 최대값 찾기
def getMax(num_list):
    return max(num_list)


# 최소값 찾기
def getMin(num_list):
    return min(num_list)


# target보다 큰 값 개수
def countGT(num_list, target):
    count = 0
    for i in num_list:
        if i > target:
            count += 1
    return count


# 리스트 합
def sumList(num_list):
    total = 0
    for i in num_list:
        total += i
    return total


# 리스트 뒤집기
def swapList(num_list):
    num_list.reverse()


# 실행 코드
number_list = [23, 45, 27, 11, 25, 65, 78]

print(getIndex(number_list, 25))
print(getMax(number_list))
print(getMin(number_list))
print(countGT(number_list, 42))
print(sumList(number_list))

swapList(number_list)
print(number_list)