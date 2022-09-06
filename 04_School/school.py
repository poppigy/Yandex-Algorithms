import math


def school():
    students = int(input())
    houses = input().split(' ')
    if students != len(houses):
        exit(1)
    if students <= 0 or students >= 100001:
        exit(1)
    # sum_h = 0
    # for house in houses:
    #     house = int(house)
    #     if house < (-2*(10**9)) or house > (2*(10**9)):
    #         exit(1)
    #     sum_h += house
    return houses[len(houses) // 2]


if __name__ == '__main__':
    print(school())
