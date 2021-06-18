#include <bits/stdc++.h>
using namespace std;

// n, m：有一个 n*m 的棋盘
// n：行,m：列
// matrix：一个字符串数组，用来记录所给矩形，matrix[i][j]表示所给矩形第i行第j列的字符（下标均从0开始）
// 返回值：题目所求答案，即最大矩形面积

int* getHistogream(int n, int m, string *matrix){
    int* height = new int[n + 2]();
        for(int i=0; i< m; i++){
            for(int j=n-1; j>=0; j--){
                if(matrix[j][i] == 'X'){
                    height[i+1] = n-j-1;
                    break;
                }
                height[i+1] = n;
            }
        }
    return height;
}

int getAnswer(int n, int m, string *matrix) {
    int area,maxArea = 0;
    stack < int > ordered;
    ordered.push(0);
    for(int i=n; i>=0; i--){
        int* height = getHistogream(i, m, matrix);
        //for(int j=0; j<=n+2; j++) cout << height[j] << "*****" << endl;
        if(accumulate(height, height + m + 1, 0) == 0) break;
        //cout << "1 pass" << endl;
        for(int j=1; j <= m+1; j++) {
            while(height[ordered.top()] > height[j]){
                int thisHight = height[ordered.top()];
                ordered.pop();
                area = thisHight * (j - ordered.top() -1);
                maxArea = max(maxArea, area);
            }
            ordered.push(j);
        }
        while(!ordered.empty()) ordered.pop();
        ordered.push(0);
    }
    return maxArea;
}
    

int main() {
    ios::sync_with_stdio(false);  // 读入优化
    
    int n, m;
    cin >> n >> m;
    
    string *matrix = new string[n]();
    
    for (int i = 0; i < n; ++i)
        cin >> matrix[i];
    
    cout << getAnswer(n, m, matrix) << endl;
    
    delete[] matrix;
    return 0;
}
