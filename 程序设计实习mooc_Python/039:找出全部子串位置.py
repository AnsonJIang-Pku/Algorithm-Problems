#source: http://cxsjsxmooc.openjudge.cn/2023pyspring/039/
#稍微卡了一会儿
n = int(input())
for i in range(n):
    [s1, s2] = input().split()
    t,x = s1.find(s2), len(s2)
    if t == -1:
        print("no")
    else:
        while t != -1:
            print(t, end = ' ')
            if t + x > len(s1) - 1:
                break
            t = s1.find(s2, t+x)
        print('')
