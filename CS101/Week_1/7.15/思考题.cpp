#include <bits/stdc++.h>
using namespace std;
char findMurderer(bool* suspicion);

bool *findMurderer(bool* suspicion){
    bool solve = 
    // Premise 1
    (suspicion[0] || suspicion[1]) &&
    // Premise 2
    (suspicion[0] + suspicion[4] + suspicion[5] == 2) &&
    // Premise 3
    !(suspicion[0] && suspicion[3]) &&
    // Premise 4
    (suspicion[1] == suspicion[2]) &&
    // Premise 5
    (suspicion[2] + suspicion[3]) && !(suspicion[2] * suspicion[3]) &&
    // Premise 6
    (!suspicion[3] && !suspicion[4]);

    if(solve) return suspicion;
    else 

    return NULL; 
}

int main(){
    bool *suspicion = findMurderer(suspicion);
    for(int i=0; i<6; i++) cout << *(suspicion + i) <<endl;
    return 0;
}