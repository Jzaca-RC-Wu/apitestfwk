import sys

sys.setrecursionlimit(10000)  # python 默认递归1000次，超过后需要手动设置递归最大值


def sum2number(n):
    if n == 1:
        return 1
    else:
        return sum2number(n - 1) + n


def get_totalfordays(n):
    if n == 1:
        return 1
    else:
        return get_totalfordays(n-1) * 2


# print(sum2number(1000))
# print(get_totalfordays(30))
for i in range(1, 30):
    print(get_totalfordays(i))