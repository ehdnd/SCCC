#include <bits/stdc++.h>
using namespace std;

void Solve() {
  string s;
  cin >> s;
  s = s.substr(0, s.length() - 2);
  s += "i";
  cout << s << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}