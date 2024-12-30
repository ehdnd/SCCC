#include <bits/stdc++.h>
using namespace std;

int N;
int prefix_sum[1010];

void Solve() {
  cin >> N;
  for (int i = 0; i < N; i++) {
    int a;
    cin >> a;
    prefix_sum[i + 1] = prefix_sum[i] + a;
  }

  int res = -1010;
  for (int i = 0; i < N; i++)
    for (int j = i; j < N; j++)
      res = max(res, prefix_sum[j + 1] - prefix_sum[i]);

  cout << res << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}