#include <bits/stdc++.h>
using namespace std;

int F, S, G, U, D;
int V[1010101];

inline bool inRange(int x) { return 1 <= x && x <= F; }

void Solve() {
  cin >> F >> S >> G >> U >> D;

  queue<int> q;
  q.push(S);
  V[S] = 1;

  while (!q.empty()) {
    int x = q.front();
    q.pop();

    if (x == G) {
      cout << V[x] - 1;
      return;
    }

    for (auto dx : {U, -D}) {
      int nx = x + dx;
      if (!inRange(nx) || V[nx]) continue;
      V[nx] = V[x] + 1;
      q.push(nx);
    }
  }

  cout << "use the stairs";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}