#include <bits/stdc++.h>
using namespace std;

struct state {int human, zombie;};
// 定义描述渡河状态东岸人数与鬼数的结构变量。
// human:人数, zombie:鬼数.

state s[20]; // 渡河状态时的状态转移过程
// 用二维向量 s_k=(human_k, zombie_k)定义为第k次渡河前东岸的渡河状态
// 安全的渡河状态集合S定义如下
state d[6] = {{0, 0}, // 0号决策不使用
              {2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}};
// 决策编号：1、2、3、4、5
int choice[20] = {0}; //记录状态转移过程的决策号，初始化都为0
int k; // 状态号

void display();
void transfer_state();

void transfer_state(){
    k = 1; //初始状态设置为1
    s[1].human = 3;
    s[1].zombie = 3;

    do{
        int fx = 1; int i; //fx:摆渡方向 i:决策号
        if(k % 2 == 1) fx = -1; //若为奇数，则为从东岸摆渡到西岸

        for(i = choice[k+1]+1; i<=5; i++){ //试探采用哪个决策能安全走一步
            int u = s[k].human + fx * d[i].human; //按i号决策走1步后，东岸的人数
            int v = s[k].zombie + fx * d[i].zombie; //按i号决策走1步后，东岸的鬼数

            if(u>3 || v>3 || u<0 || v<0) continue; //[1]状态越界。舍弃当前决策

            bool AQ = (u==3) || (u==0) || (u==v);  // 是否安全
            if(!AQ) continue; // [2]不安全。舍弃当前决策

            bool CHF = false; // 是否重复
            for(int j=k-1; j>=1; j-=2) // 若人鬼数一致，则是重复状态
                if(s[j].human == u && s[j].zombie == v) CHF = true;
            if (CHF) continue; // [3] 重复。舍弃当前决策

            k++; // 按照策略渡河，状态号加一
            s[k].human = u; s[k].zombie = v;
            choice[k] = i; // 记录决策号
            break;// 找到新的决策，跳出循环
        }
        if(i > 5) {choice[k + 1]=0; k--;} //若所有摆渡决策都未能成功，则需要回退
    } while(!(s[k].human == 0 && s[k].zombie == 0));
}

void display(){
    for(int i=1; i<=k; i++){
        cout << setw(2) << i << ": choice" << choice[i]
             << " {" << d[choice[i]].human << "," << d[choice[i]].zombie << "}"
             << " (" << s[i].human << "," << s[i].zombie << ") "
             << endl;
    }
    return;
}

int main(){
    transfer_state();
    display();
    return 0;
}