#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int N, M;
bool vis[8];
vector<int> ans, nums;

void BT(int num_cnt) {
  if (num_cnt == M) {
    for (int i : ans) cout << i << " ";
    cout << "\n";
    return;
  }

  for (int i = 0; i < N; i++) {
    if (vis[i]) continue;
    vis[i] = true;
    ans[num_cnt] = nums[i];
    BT(num_cnt + 1);

    vis[i] = false;
  }
}

void Solve() {
  cin >> N >> M;
  ans.resize(M, 0);
  nums.resize(N, 0);
  for (int& num : nums) cin >> num;

  sort(all(nums));

  BT(0);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}