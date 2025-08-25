#include <bits/stdc++.h>
using namespace std;

int T, ans;
string S;
vector<int> stk;

void Solve() {
  cin >> T;
  while (T--) {
    cin >> S;
    stk.clear();
    for (const char& c : S) {
      if (!stk.empty() && stk.back() == c) {
        stk.pop_back();
      } else {
        stk.push_back(c);
      }
    }
    if (stk.empty()) ans++;
  }
  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}