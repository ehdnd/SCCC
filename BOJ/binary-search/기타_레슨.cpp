#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<int> lengths;

bool isPoss(int size) {
  int cnt = 1, curr = 0;

  for (const int& len : lengths) {
    if (len > size) return false;

    if (curr + len > size) {
      cnt++;
      curr = len;
    } else {
      curr += len;
    }
  }

  return (cnt <= M);
}

void Solve() {
  cin >> N >> M;
  lengths.resize(N, 0);
  for (int i = 0; i < N; i++) cin >> lengths[i];

  int lo = 1, hi = 1e9;

  while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;

    if (isPoss(mid))
      hi = mid - 1;
    else
      lo = mid + 1;
  }

  cout << lo;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}