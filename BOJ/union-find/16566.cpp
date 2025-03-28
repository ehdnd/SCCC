#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int N, M, K;
vector<int> nums, query, S;

int Find(int a) { return (S[a] < 0 ? a : S[a] = Find(S[a])); }

bool Union(int a, int b) {
  a = Find(a), b = Find(b);
  if (a == b) return false;
  if (a < b) swap(a, b);
  S[a] += S[b];
  S[b] = a;
  return true;
}

void Solve() {
  cin >> N >> M >> K;
  S.resize(M, -1);
  nums.resize(M, 0);

  for (auto& val : nums) cin >> val;

  sort(all(nums));

  while (K--) {
    int q;
    cin >> q;

    auto it = upper_bound(all(nums), q);
    int idx = it - nums.begin();

    int p_idx = Find(idx);
    cout << nums[p_idx] << "\n";
    Union(p_idx, p_idx + 1);
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}