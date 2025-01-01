#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAX = 101010;
const int MAX_D = 30;  // 1'000'000'000 <= 2^30;
int N, K, M;
int student[MAX];
int table[MAX][MAX_D];

void Solve() {
  cin >> N >> K >> M;
  M--;
  for (int i = 1; i <= N; i++) cin >> student[i];

  // 시작.. table[i][j] = 정점 i 시작 2^j 이동 후 정점
  for (int i = 1; i <= K; i++) cin >> table[i][0];

  for (int j = 1; j < MAX_D; j++) {
    for (int i = 1; i <= K; i++) {
      table[i][j] = table[table[i][j - 1]][j - 1];
    }
  }

  vector<int> used_table;
  for (int j = MAX_D - 1; j >= 0; j--) {
    if (M >= 1 << j) {
      M -= (1 << j);
      used_table.push_back(j);
      //   cout << "j " << j << "\n";
    }
  }

  for (int i = 1; i <= N; i++) {
    int res = student[i];
    for (const auto& x : used_table) {
      //   cout << "x " << x << "\n";
      //   cout << "i " << i << "\n";
      //   cout << "시작 " << res << "\n";
      res = table[res][x];
      //   cout << "마지 " << res << "\n";
    }
    cout << res << " ";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}