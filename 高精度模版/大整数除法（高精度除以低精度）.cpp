#include <iostream>
#include <cstring>
#include <string>

using namespace std;
int a[220],c[500];
long long b;
//全局变量初始化的时候就自动赋值0
//高精度除以低精度, 仅输出了商的整数部分
string m;

int main()
{
    cin >> m >> b;
    int len_a = m.length();
    //竖式除法不需要倒转存储
    for(int i = 0; i < len_a; i++)
        a[i] = m[i] - '0';
    int x = 0; //记录上一次的余数
    for(int i = 0; i < len_a; i++){
        c[i] = (x * 10 + a[i]) / b;
        x = (x * 10 + a[i]) % b;
    }
    //去除前导零
    for(int i = 0; i < len_a; i++){
        if (!c[i] && i < len_a - 1)
            continue;
        cout << c[i];
    }
    return 0;
}
