#边界符号的作用：要求 整个 字符串都匹配上 ^ $
#resource: http://cxsjsxmooc.openjudge.cn/2023pyspring/051/
import re
m = "^[a-zA-Z][a-zA-Z0-9_-]{7,}$"
while True:
    try:
        s = input()
        if re.match(m,s) != None:
            print("yes")
        else:
            print("no")
    except:
        break
