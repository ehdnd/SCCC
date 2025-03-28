#include<iostream>
#include<queue>
using namespace std;
struct node{
    int x, y;
    bool operator < (const node &a) const {
        if (x == a,x) return y > a.y;
        return x > a.x;
    };
};

int main(){
    priority_queue<node>pq;
    pq.push(1);
    pq.push(1);
    pq.push(1);
    pq.push(1);
    cout << pq.top() << "\n";
}

// struct 구조체 ?