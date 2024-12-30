#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int N, M;
int pSum[101010];

void Solve() {
  cin >> N;
  for (int i = 0; i < N; i++) {
    int A;
    cin >> A;
    pSum[i + 1] = pSum[i] + A;
  }
  cin >> M;
  for (int i = 0; i < M; i++) {
    int s, e;
    cin >> s >> e;
    cout << pSum[e] - pSum[s - 1] << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}