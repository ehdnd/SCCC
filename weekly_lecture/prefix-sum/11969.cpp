#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int N, Q;
int prefix_sum[101010][3];

void Solve() {
  cin >> N >> Q;
  for (int i = 0; i < N; i++) {
    int a;
    cin >> a;
    for (int j = 0; j < 3; j++) {
      prefix_sum[i + 1][j] = prefix_sum[i][j];
    }
    prefix_sum[i + 1][a - 1]++;
  }

  while (Q--) {
    int s, e;
    cin >> s >> e;
    for (int j = 0; j < 3; j++)
      cout << prefix_sum[e][j] - prefix_sum[s - 1][j] << " ";
    cout << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}