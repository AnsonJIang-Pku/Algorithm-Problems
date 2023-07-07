//http://cxsjsxmooc.openjudge.cn/book/074/
//和题目“分解因数”很像: http://cxsjsxmooc.openjudge.cn/book/056/
n = int(input())
def ways(n, m): #要凑出数n,但最大能取到的数字是m
    if m < 1:
        return 0
    if n <= 1: #只有一种取法or不取
        return 1
    if n < m:
        return ways(n, n)
    else:
        return ways(n, m - 1) + ways(n - m, m)
print(ways(n, n))
