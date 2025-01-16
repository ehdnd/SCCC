#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int N, M;
map<int, int> nums_max, vis;
vector<int> ans;

void BT(int num_cnt) {
  if (num_cnt == M) {
    for (int i : ans) cout << i << " ";
    cout << "\n";
    return;
  }

  for (auto it = nums_max.begin(); it != nums_max.end(); it++) {
    int num = it->first;
    if (vis[num] >= nums_max[num]) continue;

    vis[num]++;
    ans[num_cnt] = num;
    BT(num_cnt + 1);
    vis[num]--;
  }
}

void Solve() {
  cin >> N >> M;
  ans.resize(M, 0);
  for (int i = 0; i < N; i++) {
    int a;
    cin >> a;
    nums_max[a]++;
  }

  BT(0);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}