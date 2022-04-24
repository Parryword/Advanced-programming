import math


def calculate1(n):
    calc = lambda a: (float(n + 1) - 3) / math.pow(float(n + 1), 2)
    total = 0
    for i in range(n):
        total += calc(n)

    return total


counter = 0


def calculate2(n):
    global counter
    total = 1

    total *= ((float(n) / (float(n) + 2)) - 10)
    counter = counter + 1

    if counter < n:
        calculate2(n-1)

    return total


if __name__ == '__main__':
    print(calculate1(5))
    print(calculate2(2))
