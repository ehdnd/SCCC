#include <bits/stdc++.h>
using namespace std;

inline int Cross(int x1, int y1, int x2, int y2) { return x1 * y2 - x2 * y1; }

void Solve() {
  int x1, x2, y1, y2, x3, y3;
  cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

  int c = Cross(x2 - x1, y2 - y1, x3 - x1, y3 - y1);

  if (c > 0)
    cout << 1;
  else if (c < 0)
    cout << -1;
  else
    cout << 0;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}