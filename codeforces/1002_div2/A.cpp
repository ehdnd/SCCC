#include <bits/stdc++.h>
using namespace std;

int N;
unordered_set<int> a, b;

void Solve() {
  cin >> N;
  a.clear();
  b.clear();

  for (int i = 0; i < N; ++i) {
    int val;
    cin >> val;
    a.insert(val);
  }

  for (int j = 0; j < N; ++j) {
    int val;
    cin >> val;
    b.insert(val);
  }

  if (a.size() == 1) {
    if (b.size() >= 3)
      cout << "YES";
    else
      cout << "NO";
  } else if (b.size() == 1) {
    if (a.size() >= 3)
      cout << "YES";
    else
      cout << "NO";
  } else {
    cout << "YES";
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