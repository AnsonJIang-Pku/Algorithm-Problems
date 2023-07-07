#http://cxsjsxmooc.openjudge.cn/book/056/
#凑出整数n,可选的最小的因数为m
def ways(n, m): #与“整数的加法分解“不同，要从小到大递归
    global ans
    for i in range (m, n+1):
        if n % i == 0:
            ways(n//i, i)
        if n == i:
            ans += 1
    
n = int(input())
for i in range (n):
    ans = 0
    x = int(input())
    ways(x, 2)
    print(ans)
