#include <bits/stdc++.h>
using namespace std;

int N, M, ma, mb, sa, sb, tmp, n_A[101];
vector<int> A, B, ans;

void Solve() {
  cin >> N;
  A.resize(N);
  for (int& x : A) cin >> x;

  cin >> M;
  B.resize(M);
  for (int& x : B) cin >> x;

  while (1) {
    if (sa == N || sb == M) break;

    ma = tmp = -1;
    bool flag = false;

    for (int i = sa; i < N; ++i) {
      if (n_A[A[i]]) continue;

      if (ma < A[i]) {
        ma = A[i];
        tmp = i + 1;
      }
    }

    if (tmp == -1) break;

    for (int i = sb; i < M; ++i) {
      if (B[i] == ma) {
        sb = i + 1;
        flag = true;
        break;
      }
    }

    if (flag) {
      ans.push_back(ma);
      sa = tmp;
    } else {
      n_A[ma] = 1;
    }
  }

  cout << ans.size() << "\n";
  for (const int& x : ans) cout << x << " ";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}