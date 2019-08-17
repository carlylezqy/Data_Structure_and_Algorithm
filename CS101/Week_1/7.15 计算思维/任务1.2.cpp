#include <bits/stdc++.h>
using namespace std;

int num = 0; // 方案数

int take[99]; // 方案细节
const int TARGET_H = 5;
int path[TARGET_H]; // 方案细节

void Downstairs_A(int i,int start);
void Downstairs_B(int height, int step);

void Downstairs_A(int i,int start){
    // i: i级台阶 j: 即将下降的台阶数
    // start: 从第start步开始
    for(int j=3; j>0; j--){
        if(i >= j){
            take[start] = j;
            if(i == j){ // 到楼下
                num++;
                cout << "Case " << num << ":";
                for (int k=1; k<=start; k++) cout << take[k] << ' ';
                cout << endl;
    
            } else Downstairs_A(i-j, start+1);
        }
    }
}

void Downstairs_B(int height, int step){
// 先判断中止，再枚举递归
// 第step步，从高度height开始，继续下楼
    if (height == 0){ // 到楼下
        num++;
        cout << "Case " << num << ":";
        for(int i=0; i<step; i++) cout << path[i] << ' ';
        cout << endl;
        return;
    }
    // 依次尝试不同的下楼步数（i）
    for(int i=1; i<=3; i++){
        int new_height = height - i; // 新高度
        if(new_height < 0) continue; // 是否合法
        path[step] = i; // 当前步数记录到方案细节之中
        Downstairs_B(new_height, step+1); // 继续下降
    }
}

int main(){
    cout << "台阶数:";
    int h;
    cin >> h;

    cout << "[Method_A]" << endl;
    Downstairs_A(h, 1); // 从第h级，开始下第一步
    num = 0; // 方案数初始化
    cout << "[Method_B]" << endl;
    Downstairs_B(TARGET_H, 0);
    // 第0步，从高度 TARGET_H 出发
    cout << "总方案数：" << num << endl;
    return 0;
}
