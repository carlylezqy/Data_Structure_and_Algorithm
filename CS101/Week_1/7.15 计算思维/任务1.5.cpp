#include <bits/stdc++.h>
using namespace std;

int Num;
int Q[9];
bool S[9];
bool L[17];
bool R[17];
const int OFFSET = 9;
void EightQueens(int col);

int main(){
    Num = 0;
    for(int i=0; i<9; i++) S[i] = true;
    for(int i=0; i<17; i++) L[i] = R[i] = true;

    EightQueens(1);

    return 0;
}

void EightQueens(int col){
    if(col == 9){
        Num++;
        cout << "方案" << Num << ":";
        for(int k=1; k<=8; k++) cout << Q[k] << "";
        cout << endl;
        return;
    }
    for(int row=1; row<=8; row++){
        if(!S[row] || !R[col + row] || !L[col - row + OFFSET]) continue;
        Q[col] = row;

        S[row] = false;
        L[col - row + OFFSET] = false;
        R[col + row] = false;

        EightQueens(col + 1);

        S[row] = true;
        L[col - row + OFFSET] = true;
        R[col + row] = true;
    }
}