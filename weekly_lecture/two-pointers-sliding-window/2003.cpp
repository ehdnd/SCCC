#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int n, m;
int A[10000];
int lo, hi;
int res, sum;

void Solve() {
  cin >> n >> m;
  for (int i = 0; i < n; i++) cin >> A[i];

  while (1) {
    // 1. 전체 부분합이 M이상 -> lo++
    if (sum >= m) sum -= A[lo++];
    // 3. e가 n에 도달 -> 종료
    else if (hi == n)
      break;
    // 2. 그게 아니라면 hi++
    else
      sum += A[hi++];

    // 부분합 == M -> res++
    if (sum == m) res++;
  }
  cout << res;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}