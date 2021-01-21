//
// Created by CauJoeng on 2019/8/23.
//

#include <bits/stdc++.h>
using namespace std;

int dx[] = {1, 2, 2, 1}, dy[] = {2, 1, -1, -2};
int num, path[100][2];

void Jump(int x, int y, int step);

int main(){
    num = 0; //初始方案数置于 0
    Jump(0, 0, 0); //第0步，从(0, 0)出发
    return 0;
}

void Jump(int x,int y,int step) {
    if((x == 8) && (y ==4)) { // 是否到达目标
        num ++; // 方案数叠加
        cout << num << ": ";
        for(int i=0; i<step; i++) // 从起点开始输出各步的坐标
            cout << "(" << path[i][0] << ", " << path[i][1] << ") ";
        cout << endl;
        return;
    }

    // 遍历四种跳步方向
    for(int k=0; k<4; k++){
        int x1 = x + dx[k], y1 = y + dy[k];
        // (x1, y1) 是否合法
        if((x1 < 0) || (x1 > 8) || (y1 < 0) || (y1 > 4)) continue;
        path[step][0] = x1;
        path[step][1] = y1;

        // 跳一步，探索不同的跳步方案
        Jump(x1, y1, step+1);
    }
}