# 斐波那契数列
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
def fibonacci(n):
    a = [0, 1, 1]
    if n < 0:
        print('n is out of range!')
    elif n < 3:
        return a[n]
    for i in range(3, n+1):
        a.append(a[i-1]+a[i-2])
    return a

print(fibonacci(9))