//
// Created by CauJoeng on 2019/8/23.
//

#include <bits/stdc++.h>
using namespace std;

int like[5][5] = {
    {0, 0, 1, 1, 0},
    {1, 1, 0, 0, 1},
    {0, 1, 1, 0, 1},
    {0, 0, 0, 1, 0},
    {0, 1, 0, 0, 1},
};
int num;
int assigned[5]; // assigned[book_id] = reader_id。其中reader_id为-1时表示未分配。

struct assign_state{int assigned[5];} state;

void normal_distribute(int reader);
void without_backtracking_distribute(int reader, assign_state state);

int main() {
    num = 0; // 设置分书方案初始值为0
    // 将所有书本状态设置为未分配
    for (int book=0; book<5; book++) assigned[book] = -1;
    normal_distribute(0); //从第0个读者开始，寻找所有发分书方案

    num = 0; 
    for (int book=0; book<5; book++) assigned[book] = -1;
    without_backtracking_distribute(0, state); 
    return 0;
}

void normal_distribute(int reader){
    if(reader == 5){
        num ++;
        cout << "第" << num << "个方案: ";
        for (int i=0; i<5; i++) cout << assigned[i] << ' ';
        cout << endl;
        return;
    }

    for(int book=0; book<5; book++){
        if((like[reader][book] != 1) || assigned[book] != -1) continue;
        assigned[book] = reader; // 记录当前这本书的分配情况
        normal_distribute(reader+1); // 为下一位读者分配合适的书籍
        assigned[book] = -1; // 将书退还（回溯），尝试另外一种方案。
    
    }
}

void without_backtracking_distribute(int reader, assign_state state){
    if(reader == 5){
        num ++;
        cout << "第" << num << "个方案: ";
        for (int i =0; i<5; i++) cout << state.assigned[i] << ' ';
        cout << endl;
        return;
    }
    for(int book=0; book<5; book++){
        if((like[reader][book] != 1) || state.assigned[book] != -1) continue;
        assign_state next_state = state; // 产生新的状态变量
        next_state.assigned[book] = reader;
        without_backtracking_distribute(reader+1, next_state); // 为下一位读者分配合适的书籍
    }
}
