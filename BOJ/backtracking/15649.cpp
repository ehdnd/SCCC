#include <bits/stdc++.h>
using namespace std;

int N, M;
bool used[9];
vector<int> ans;

void BackTracking(int num_cnt) {
  if (num_cnt == M) {
    for (int i : ans) cout << i << " ";
    cout << "\n";
    return;
  }

  for (int i = 1; i <= N; i++) {
    if (used[i]) continue;

    used[i] = 1;
    ans[num_cnt] = i;
    BackTracking(num_cnt + 1);

    used[i] = 0;
  }
}

void Solve() {
  cin >> N >> M;
  ans.resize(M, 0);

  BackTracking(0);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}