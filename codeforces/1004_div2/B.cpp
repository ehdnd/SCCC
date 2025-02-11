#include <bits/stdc++.h>
using namespace std;

const int MAX = 101010;

void Solve() {
  int N;
  cin >> N;
  vector<int> cnts(N + 1, 0);
  for (int i = 0; i < N; ++i) {
    int val;
    cin >> val;
    cnts[val]++;
  }

  for (int i = 1; i <= N; ++i) {
    if (cnts[i] == 0) continue;
    if (cnts[i] == 1) {
      cout << "No\n";
      return;
    }

    cnts[i + 1] += cnts[i] - 2;
  }

  cout << "Yes\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}