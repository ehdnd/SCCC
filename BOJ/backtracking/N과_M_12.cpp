#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int N, M;
vector<int> nums, ans;

void BT(int num_cnt, int st) {
  if (num_cnt == M) {
    for (int num : ans) cout << num << " ";
    cout << "\n";
    return;
  }

  int last_used = -1;

  for (int i = st; i < N; i++) {
    if (nums[i] == last_used) continue;

    ans[num_cnt] = nums[i];
    BT(num_cnt + 1, i);

    last_used = nums[i];
  }
}

void Solve() {
  cin >> N >> M;
  nums.resize(N);
  ans.resize(M);
  for (int i = 0; i < N; i++) {
    cin >> nums[i];
  }

  sort(all(nums));
  BT(0, 0);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}
