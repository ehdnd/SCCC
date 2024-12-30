#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int N, Q, prev_a;
int prefix_sum[1010];

void Solve() {
  cin >> N >> Q;
  cin >> prev_a;
  for (int i = 0; i < N - 1; i++) {
    int a;
    cin >> a;
    prefix_sum[i + 1] = prefix_sum[i] + abs(prev_a - a);
    prev_a = a;
  }
  for (int i = 0; i < Q; i++) {
    int s, e;
    cin >> s >> e;
    if (e - 1 < s)
      cout << 0 << "\n";
    else
      cout << prefix_sum[e - 1] - prefix_sum[s - 1] << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}