#debug有点痛苦
#source: http://cxsjsxmooc.openjudge.cn/2023pyspring/054/
import re
n = int(input())
#首先抽取tag,不论其内部是否有电话号码
regex1 = r"<([a-z]+)>(.+?)</\1>"
regex2 = "\(\d{1,2}\)-\d{3,}"
regex3 = "\(\d{1,2}\)" #提取出区号用
for i in range(n):
    s = input()
    ans = re.findall(regex1, s)
    flag = 0
    #ans形如[('abc', 'nn(01)-123sszc(0)-124dffs'), ('x', 'xz(0)-1234xzas'), ...]
    for subs in ans:
        mid = ''
        res = re.findall(regex2, subs[1])
        #res形如['(01)-123', '(0)-124', ...]
        if res != []:
            for ele in res:
                #print("test:", ele)
                #保证是电话号码：最多八位
                if len(ele) > 8:
                    continue
                x = re.match(regex3, ele)
                if len(x.group()) == 3:
                    #添加两个tag之间的字符
                    mid += x.group()[1] + ','
                else:
                    mid += x.group()[1:3] + ','
            if mid != '':
                flag = 1
                mid = mid[:-1]
                string = '<' + subs[0] + '>' + mid + "</" + subs[0] + '>'
                print(string)
    if flag == 0:
        print("NONE")
