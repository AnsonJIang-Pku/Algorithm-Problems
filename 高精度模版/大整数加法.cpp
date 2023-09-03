//source: http://bailian.openjudge.cn/practice/2981/

#include <iostream>
#include <cstring>
#include <string>

using namespace std;
int a[220],b[220],c[220];
//全局变量初始化的时候就自动赋值0
string m,n;

int main()
{
    cin >> m >> n;
    int len_a = m.length(), len_b = n.length(), len_c;
    //将m和n倒序装入数组a和b
    for(int i = 0; i < len_a; i++)
        a[len_a - i] = m[i] - '0';
    for(int i = 0; i < len_b; i++)
        b[len_b - i] = n[i] - '0';
    //进行竖式加法
    len_c = max(len_a, len_b) + 1;
    for(int i = 0; i < len_c; i++){
        c[i] += a[i] + b[i];
        c[i+1] = c[i] / 10;
        c[i] %= 10;
    }
    //删除前导零
    //考虑到0+0=0必须显示,将长度设定为>0
    int i = len_c;
    while(!c[i] && i > 1)
        i--;
    for(; i > 0; i--)
        cout << c[i];
    return 0;
}
