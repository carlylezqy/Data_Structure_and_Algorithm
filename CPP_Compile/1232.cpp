#include <iostream>
using namespace std;

int main()
{
    int coordinates[6][2] = {{1,2},{2,3},{3,4},{4,5},{5,6},{6,7}};

    int x1 = coordinates[0][0];
    cout << x1 << endl;

    int y1 = coordinates[0][1];
    int x2 = coordinates[1][0];
    int y2 = coordinates[1][1];
    int i = 0;

    for(i=1; i<coordinates.size(); i++){
        int x = coordinates[i][0];
        int y = coordinates[i][1];
        if(x2 == x1 or y2 == y1){
            if((x2 == x1 and x != x1) or (y2 == y1 and y != y1)){
                cout << "False" <<endl;
                return 0;
            }
        } else {
            if ((x - x1)/(x2 - x1) != (y - y1)/(y2 - y1)){
                cout << "False" <<endl;
                return 0;
            }
        }
        
    }
    cout << "True" <<endl;
    return 1;
}