#include <bits/stdc++.h>
using namespace std;

stack<int> sorting(stack<int>);

int main() {
    int n;
    cin >> n;
    stack<int> myStack;
    for (int i = 0; i < n; ++i) {
        int tmp;
        cin >> tmp;
        myStack.push(tmp);
    }
    
    stack<int> result = sorting(myStack);
    
    vector<int> answer;
    while (!result.empty()) {
        answer.insert(answer.begin(),result.top()); 
        //answer.push_back(result.top());
        result.pop();
    }
    for (auto i = answer.rbegin(); i != answer.rend(); ++i)
        cout << *i << endl;
    return 0;
}

// myStack：输入栈，栈中的所有元素即是待排序的元素
// 返回值：输出栈，即排序后的序列，满足从栈底至栈顶为升序
stack<int> sorting(stack<int> myStack) {
    stack<int> ordered;
    int tmp = 0;
    int size = myStack.size();
    ordered.push(myStack.top());
    myStack.pop();
    while(!myStack.empty() && ordered.size() < size){
        tmp = myStack.top();
        myStack.pop();
        if(ordered.empty() || tmp <= ordered.top()){
            ordered.push(tmp);
        }else{
            while(!ordered.empty() && tmp > ordered.top()){
                myStack.push(ordered.top());
                ordered.pop();
            }
            ordered.push(tmp);
        }
    }
    return ordered;
}