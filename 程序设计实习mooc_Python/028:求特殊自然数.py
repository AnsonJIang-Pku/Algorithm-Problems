#source: http://cxsjsxmooc.openjudge.cn/2023pyspring/028/
#use definition!!!
max = 6* 7**2 + 6*7 + 6 #最大的三位七进制数
for x in range(1, max + 1):
    c, b, a = x%7, (x//7)%7, (x//49)%7
    if c* 9**2 + b*9 + a == x:
        break
print(x)
print("%d%d%d" % (a,b,c))
print("%d%d%d" % (c,b,a))
