#include <bits/stdc++.h>
using namespace std;

struct cups {int A, B, C;};
bool visit [80][80][80];
int capacity[3] = {80, 50 ,30};

struct init_state(){
cups cup = {80, 0, 0};
memset(visit, 0, sizeof(visit));
return cup;
}

bool is_invalid_state(cups cup){
    if(cup.A > capacity[0] || cup.B > capacity[1] || cup.c > capacity[2]) return true;
    if(cup.A < 0 || cup.B < 0 || cup.c < 0) return true;
    if(cup.A + cup.B + cup.c == 80) return true;
    return false;
}

bool is_final_state(cups cup){
    if(cup.A == 40 && cup.B == 40) return true;
    return false;
}

bool is_processed(cups cup){
    if(visit[cup.A][cup.B][cup.C]) return true;
    return false;
}

bool search(cups cup){
    if(is_invalid_state(cup)) return false;
    if(is_final_state(cup)){
        return true;
    }
    if(is_processed(cup)) return false;

    if(search({cup.A - capacity[1], capacity[1], cup.C})) return ture;
    if(search({cup.A - capacity[2], cup.B, capacity[2]})) return ture;
    if(search({cup.A - capacity[2], cup.B, capacity[2]}) return ture;

    return false;
}

int main(){
    cups cup = init_state(cup);
    search(cup);
    return 0;
}