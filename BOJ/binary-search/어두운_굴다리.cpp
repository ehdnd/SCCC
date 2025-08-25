#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int N, M;
vector<int> A;

bool isPoss(int h) {
  if (h < A[0]) return false;
  if (A[M - 1] + h < N) return false;

  for (int i = 0; i < M - 1; ++i) {
    if (A[i] + h < A[i + 1] - h) return false;
  }
  return true;
}

void Solve() {
  cin >> N >> M;
  A.resize(M, 0);
  for (int& x : A) cin >> x;

  int lo = 0;
  int hi = N;

  while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;

    if (isPoss(mid)) {
      hi = mid - 1;
    } else {
      lo = mid + 1;
    }
  }

  cout << lo;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}