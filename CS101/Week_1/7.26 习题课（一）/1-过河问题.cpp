//
// Created by CauJoeng on 2019/8/26.
//

#include <bits/stdc++.h>
using namespace std;

struct state {int Human, Wolf, Sheep, Vegetable;};
char history[30];

state cross_river(state s, char carry){
    s.Human = 1 - s.Human;
    if(carry == '-'){
    } else if (carry == 'W'){
        s.Wolf = 1 - s.Wolf;
    } else if (carry == 'V'){
        s.Vegetable = 1 - s.Vegetable;
    } else if (carry == 'S'){
        s.Sheep = 1 - s.Sheep;
    } else {
        assert(0);
    }
/*
    switch(carry){
    case '-':break;
    case 'W':s.Wolf = 1 - s.Wolf;break;
    case 'V':s.Vegetable = 1 - s.Vegetable;break;
    case 'S':s.Sheep = 1 - s.Sheep;break;
    default: assert(0);

}
*/
    return s;
}

bool is_invalid_state(state s){
    if(s.Human != s.Sheep && s.Sheep == s.Wolf) return true;
    if(s.Human != s.Sheep && s.Sheep == s.Vegetable) return true;
    return false;
}

void show_history(int n){
    for(int i=0; i<n; i++)
        cout << "H";
        if(history[n] != '-')
            cout << "_" << history[n];
    puts("");
    return;
}

bool is_final_state(state s){
    if(s.Human == 1 && s.Wolf == 1 && s.Sheep == 1 && s.Vegetable == 1) return true;
    else return false;
}

bool visit[2][2][2][2];
bool solve(state s, int step){
    //cout << s.Human << " " << s.Wolf << " " <<  s.Sheep <<  " " << s.Vegetable <<endl;

    if(is_invalid_state(s)) return false;
    if(is_final_state(s)) {
        //show_history(step);
        return true;
    }
    if(visit[s.Human][s.Wolf][s.Sheep][s.Vegetable] == true) return false;

    visit[s.Human][s.Wolf][s.Sheep][s.Vegetable] = true;

    state next_state;

    next_state = cross_river(s, '-');
    cout << '-';
    if(solve(next_state,step + 1)) return true;

    if(s.Human == s.Wolf){
        cout << 'W';
        next_state = cross_river(s, 'W');
        if(solve(next_state,step + 1)) return true;
    }

    if(s.Human == s.Sheep){
        cout << 'S';
        next_state = cross_river(s, 'S');
        if(solve(next_state,step + 1)) return true;
    }

    if(s.Human == s.Vegetable){
        cout << 'V';
        next_state = cross_river(s, 'V');
        if(solve(next_state,step + 1)) return true;
    }

    return false;
}

int main(){
    memset(visit, 0, sizeof(visit));
    state init_state = {0, 0, 0, 0};
    solve(init_state, 0);
    return 0;
}