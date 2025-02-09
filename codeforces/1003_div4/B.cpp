#include <bits/stdc++.h>
using namespace std;

void Solve() {
  string s;
  cin >> s;

  bool flag = false;
  char p = s[0];

  for (int i = 1; i < s.length(); ++i) {
    char c = s[i];
    if (p == c) {
      flag = true;
      break;
    }
    p = c;
  }

  cout << (flag ? 1 : s.length()) << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}