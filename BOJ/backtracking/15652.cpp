#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<int> ans;

void BT(int num_cnt, int st) {
  if (num_cnt == M) {
    for (int i : ans) cout << i << " ";
    cout << "\n";
    return;
  }

  for (int i = st; i <= N; i++) {
    ans[num_cnt] = i;
    BT(num_cnt + 1, i);
  }
}

void Solve() {
  cin >> N >> M;
  ans.resize(M);

  BT(0, 1);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}