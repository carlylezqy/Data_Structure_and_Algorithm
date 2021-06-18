#include <bits/stdc++.h>
using namespace std;

int Num; // 方案数
int Q[9]; // 8个皇后所占用的行号
bool S[9], L[17], R[17]; //S[]：检查当前行是否安全。L[]：(i-j)对角线是否安全。R[]：(i+j)对角线是否安全
const int OFFSET = 9; //统一数组下标范围[2, 3, ..., 16]

struct place_state{
    int Q[9];
    bool S[9], L[17], R[17];
};

void EightQueens(int col);

int main(){
    Num = 0;
    for(int i=0; i<9; i++) S[i] = true;
    for(int i=0; i<17; i++) L[i] = R[i] = true;

    EightQueens(1); // 尝试从第一列开始放置皇后

    return 0;
}

void EightQueens(int col){
    if(col == 9){ // 递归终止条件
        Num++;
        cout << "方案" << Num << ":";
        for(int k=1; k<=8; k++) cout << Q[k] << "";
        cout << endl;
        return;
    }
    for(int row=1; row<=8; row++){ // 依次尝试当前列的8行位置
        if(!S[row] || !R[col + row] || !L[col - row + OFFSET]) continue;
        Q[col] = row; //记录位置信息（行号）

        // 修改三个方向的安全标记
        S[row] = L[col - row + OFFSET] = R[col + row] = false;

        EightQueens(col + 1); //递归尝试放下一列

        // 【回溯】恢复三个方向原有安全性
        S[row] = L[col - row + OFFSET] = R[col + row] = true;
    }
}

void without_backtracking_EightQueens(int col, place_state state){
    if(col == 9){ // 递归终止条件
        Num++;
        cout << "方案" << Num << ":";
        for(int k=1; k<=8; k++) cout << Q[k] << "";
        cout << endl;
        return;
    }

    for(int row=1; row<=8; row++){
        if(!state.S[row] || !state.R[col+row] || !state.L[col-row+OFFSET]) continue;
        place_state.Q[col] = row; // 记录位置信息（行号）

        // 新的状态变量中，记录三个方向的安全性
        next_state.S[row] = next_state.L[col-row+OFFSET] = next_state.R[col+row] = false;

        // 递归尝试放下一列
        without_backtracking_EightQueens(col+1, next_state);
    }
}