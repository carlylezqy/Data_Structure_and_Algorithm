#include <bits/stdc++.h>
using namespace std;

char basic_method(){
    char thisMan = '?';
    int sum = 0;
    thisMan = 'A';
    sum = (thisMan != 'A') + (thisMan == 'C') 
        + (thisMan == 'D') + (thisMan != 'D');
    if(sum == 3) return thisMan;
    
    thisMan = 'B';
    sum = (thisMan != 'A') + (thisMan == 'C') 
        + (thisMan == 'D') + (thisMan != 'D');
    if(sum == 3) return thisMan;

    thisMan = 'C';
    sum = (thisMan != 'A') + (thisMan == 'C') 
        + (thisMan == 'D') + (thisMan != 'D');
    if(sum == 3) return thisMan;

    thisMan = 'D';
    sum = (thisMan != 'A') + (thisMan == 'C') 
        + (thisMan == 'D') + (thisMan != 'D');
    if(sum == 3) return thisMan;

    return thisMan;
}

char modified_method(){
    char translate[4] = {'A','B','C','D'};
    int sum = 0;
    
    for(int thisMan=0; thisMan<4; thisMan++){
        sum = (thisMan != 0) + (thisMan == 2) 
            + (thisMan == 3) + (thisMan != 3);
        if(sum == 3) return translate[thisMan];
    }

    return '?';
}


int main(){
    cout << basic_method() << endl;
    cout << modified_method() << endl;
    return 0;
}