#关键在于如何取出所有长度至少为2的所有子串：直接用端点取很容易数不清
#利用长度遍历，越界剪枝
#source: http://cxsjsxmooc.openjudge.cn/2023pyspring/046/
def is_palindrom(s):
    if s == s[::-1]:
        return 1
    else:
        return 0

s = input()
n = len(s) #按照长度遍历,而不是直接指定起止点i,j
ans = []
for i in range (1,n+1):
    for j in range(n):
        if j + i > n-1:
            continue
        if is_palindrom(s[j:j+i+1]):
            ans.append(s[j:j+i+1])
ans.sort(key = lambda s: len(s))
for strs in ans:
    print(strs)
