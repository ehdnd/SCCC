#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int N;
vector<vector<int>> paper;
int cnt[2];

void DivideAndConquer(int n, int x, int y) {
  if (n == 1) {
    cnt[paper[x][y]]++;
    return;
  }

  bool isDiff = false;
  int now = paper[x][y];

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (paper[x + i][y + j] != now) {
        isDiff = true;
      }
    }
  }

  if (isDiff) {
    DivideAndConquer(n / 2, x, y);
    DivideAndConquer(n / 2, x + n / 2, y);
    DivideAndConquer(n / 2, x, y + n / 2);
    DivideAndConquer(n / 2, x + n / 2, y + n / 2);
  } else {
    cnt[paper[x][y]]++;
  }
}

void Solve() {
  cin >> N;
  paper.resize(N, vector<int>(N));
  for (auto& row : paper)
    for (auto& val : row) cin >> val;

  DivideAndConquer(N, 0, 0);

  cout << cnt[0] << "\n" << cnt[1];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}