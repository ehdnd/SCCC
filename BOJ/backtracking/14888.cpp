#include <bits/stdc++.h>
using namespace std;

const int INF = 2e9;

int N, a_min, a_max;
vector<int> nums;
int ops[4], used[4];

void Dfs(int idx, int curr) {
  if (idx == N) {
    a_min = min(a_min, curr);
    a_max = max(a_max, curr);
    return;
  }

  for (int op = 0; op < 4; ++op) {
    if (used[op] >= ops[op]) continue;

    int temp = curr;

    used[op]++;

    if (op == 0) {
      temp += nums[idx];
    } else if (op == 1) {
      temp -= nums[idx];
    } else if (op == 2) {
      temp *= nums[idx];
    } else {
      temp /= nums[idx];
    }

    Dfs(idx + 1, temp);

    used[op]--;
  }
}

void Solve() {
  cin >> N;
  nums.resize(N, 0);
  for (int& n : nums) cin >> n;
  for (int i = 0; i < 4; ++i) cin >> ops[i];

  a_min = INF, a_max = -INF;

  Dfs(1, nums[0]);

  cout << a_max << "\n" << a_min;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}