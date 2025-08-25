#include <bits/stdc++.h>
using namespace std;

int cnt, sz;

void BT(vector<int> rems, int idx, int p) {
  if (idx == sz) {
    cnt++;
    return;
  }

  for (int i = 0; i < 26; ++i) {
    if (rems[i] && i != p) {
      rems[i]--;
      BT(rems, idx + 1, i);
      rems[i]++;
    }
  }
}

void Solve() {
  string S;
  cin >> S;
  sz = S.size();

  vector<int> A(26, 0);
  for (char& c : S) A[c - 'a']++;

  BT(A, 0, -1);

  cout << cnt;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}