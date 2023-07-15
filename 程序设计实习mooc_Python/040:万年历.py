#source: http://cxsjsxmooc.openjudge.cn/2023pyspring/040/
def f(x):
    if x == 0:
        print("Monday")
    elif x == 1:
        print("Tuesday")
    elif x == 2:
        print("Wednesday")
    elif x == 3:
        print("Thursday")
    elif x == 4:
        print("Friday")
    elif x == 5:
        print("Saturday")
    elif x == 6:
        print("Sunday")

def check(y,m,d):
    if not(-1000000 <= y <= 1000000) or not(1 <= m <= 12):
        print("Illegal")
        return 0
    else:
        if (y % 100 != 0 and y % 4 == 0) or y % 400 == 0:
            days_list[1] = 29
        if not(1 <= d <= days_list[m-1]):
            print("Illegal")
            return 0
    return 1

n = int(input())
days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(n):
    days_list[1] = 28
    y, m, d = map(int, input().split())
    #check date:
    if check(y,m,d):
        #cal date:
        if (y,m,d) == (-1000000,1,1):
            print("Saturday")
        elif (y,m,d) == (-1000000,1,2):
            print("Sunday")
        ans = 0
        for year in range(-1000000, y):
            if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
                ans += 366
            else:
                ans += 365
        for month in range(0, m-1):
            ans += days_list[month]
        ans += d-3
        f(ans%7)
