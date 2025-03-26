#include <bits/stdc++.h>
using namespace std;

int N, last;
int rep[] = {2, 1, 2, -1};

void Solve() {
  cin >> N;
  cout << "YES\n";

  if (N == 3) {
    cout << "2 1 3 ";
    return;
  }

  last = -1;

  if ((N % 4) == 2) {
    cout << "2 1 ";
    last = 1;
  }

  if ((N % 4) == 3) {
    cout << "1 3 2 ";
    last = 2;
  }

  for (int i = 0; i < N / 4; ++i) {
    for (int dx : rep) {
      last += dx;
      cout << last << " ";
    }
  }

  if ((N % 4) == 1) {
    cout << last + 2;
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}