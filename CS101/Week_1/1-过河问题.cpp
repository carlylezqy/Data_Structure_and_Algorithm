#include <bits/stdc++.h>
using namespace std;

void remove(int *data, int idx);
bool checkSafe(int *wt2);

void remove(int *data, int idx)
{
    int len = sizeof(*&data);
    len--;
    if (idx < 0 || idx >= len)
        return;
    for (int i = idx; i < len; i++)
        data[i] = data[i+1];
}

bool checkSafe(int *wt2){
    bool isWexist,isSexist,isVexist = false;
    for(int i=0; i<sizeof(wt2); i++){
        switch(wt2[i]){
            case 1:
                if(isWexist) return false;
                isWexist=true; 
                break;
            case 2:
                if(isSexist) return false;
                isSexist=true; break;
            case 3:
                if(isVexist) return false;
                isVexist=true; break;
        }
    }
    if(isWexist && isSexist) return false;
    if(isSexist && isVexist) return false;
    return true;
}

int main(){
    char AAA[4] = {'H','W','S','V'};
    char wt2Depart[8] = {'1','2','3'};
    char wt2Return[8] = {};
    int *result = new string[4]();

    for(int i=1; i<4; i++){
        for(int j=0; j<4; j++){
            for(int k=1; k<4; k++){
                for(int l=0; l<4; l++){
                    result[] = {i,j,k,l};
                    if(checkSafe(){
                        cout << result;
                    }
                }
            }
        }

    }
    return 0;
}