#边界条件不好想全
#source: http://cxsjsxmooc.openjudge.cn/2023pyspring/031/
def ways(m, n, s):
    if m > s:
        return ways(s, n, s)
    else:
        if m == 0 and (n != 0 or s != 0):
            return 0
        if n == 0 and s > 0:
            return 0
        if n == 0 and s == 0:
            return 1
        if m != 0 and (n != 0 and s == 0):
            return 0
        return ways(m-1, n-1, s-m) + ways(m-1, n, s)

t = int(input())
for i in range(t):
    m, n, s = map(int, input().split())
    print(ways(m,n,s))
