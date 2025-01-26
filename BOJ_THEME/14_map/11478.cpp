#include <bits/stdc++.h>
using namespace std;

string S;
unordered_set<string> subsets;

void Solve() {
  cin >> S;
  int length = S.length();
  for (int st = 0; st < length; st++)
    for (int cnt = 0; cnt < length; cnt++) subsets.insert(S.substr(st, cnt));

  cout << subsets.size();
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}