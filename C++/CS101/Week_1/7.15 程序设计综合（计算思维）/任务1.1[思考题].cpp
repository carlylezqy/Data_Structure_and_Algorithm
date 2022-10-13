#include <bits/stdc++.h>
using namespace std;
bool *findMurderer(bool* suspicion);

bool *findMurderer(bool* suspicion){

    for(int i=0; i<64; i++){
        int dec = i;
        int order = 0;
        int transfer[6] = {0};

        while(order < 6 && dec>0){
            if(dec%2 == 1){
                suspicion[order] = true;
                transfer[order] = 1;
            }
            else suspicion[order] = false;
            order++;
            dec = dec / 2;
        }

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
    }
    return NULL;
}

int main(){
    bool suspicion[6] = {false, false, false, false, false, false};
    char name[6] = {'A', 'B', 'C', 'D', 'E', 'F'};
    findMurderer(suspicion);

    for(int i=0; i<6; i++)
        if(suspicion[i]) cout << name[i] << ' ';

    cout << endl;
    return 0;
}

