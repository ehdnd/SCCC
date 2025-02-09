#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

void Solve() {
  int N, M, B;
  cin >> N >> M;

  vector<int> A(N, 0), AA(N, 0);

  for (int& a : A) cin >> a;
  cin >> B;

  for (int i = 0; i < N; ++i) {
    AA[i] = B - A[i];
  }

  bool isPoss = true;
  int p = min(A[0], AA[0]);

  for (int i = 1; i < N; ++i) {
    int c = INF;

    if (p <= A[i]) {
      c = A[i];
    }
    if (p <= AA[i]) {
      c = min(c, AA[i]);
    }

    if (c == INF) {
      isPoss = false;
      break;
    }

    p = c;
  }

  cout << (isPoss ? "YES" : "NO") << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}