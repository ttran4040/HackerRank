testcase = int(raw_input())

def UCLN(x, y):
    if x % y == 0: return y
    return UCLN(y, x % y)

for i in range(testcase):
    (x, y) = raw_input().split()
    x = int(x)
    y = int(y)
    print x * y / (UCLN(x, y) ** 2)
