#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

void Solve() {
  int x, y;
  cin >> x >> y;

  if (y - x == 1) {
    cout << "Yes";
  } else if ((x - y) % 9 == 8) {
    cout << "Yes";
  } else {
    cout << "No";
  }
  cout << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}