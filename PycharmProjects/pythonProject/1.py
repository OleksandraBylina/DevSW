n = 234
m = 345
def colon(n, m, i = 0):
    if n == 0 and m == 0:
        return 0
    else:
        return colon(n // 10, m // 10, i + 1) + (m % 10 + n % 10) * 10 ** i



print(colon(n, m))