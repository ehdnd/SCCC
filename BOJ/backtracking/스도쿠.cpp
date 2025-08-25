#include <bits/stdc++.h>
using namespace std;

int ans[9][9];
bool used_row[9][10], used_col[9][10], used_mat[3][3][10], isSolved;

void BT(int r, int c) {
  if (r == 9) {
    isSolved = true;
    return;
  }

  if (c == 9) BT(r + 1, 0);

  if (ans[r][c]) {
    BT(r, c + 1);
    return;
  }

  for (int i = 1; i <= 9; ++i) {
    if (used_row[r][i] || used_col[c][i] || used_mat[r / 3][c / 3][i]) continue;

    ans[r][c] = i;
    used_row[r][i] = used_col[c][i] = used_mat[r / 3][c / 3][i] = true;
    BT(r, c + 1);

    if (isSolved) return;

    ans[r][c] = 0;
    used_row[r][i] = used_col[c][i] = used_mat[r / 3][c / 3][i] = false;
  }
}

void Solve() {
  for (int r = 0; r < 9; ++r) {
    string row;
    cin >> row;
    for (int c = 0; c < 9; ++c) {
      int val = row[c] - '0';
      ans[r][c] = val;

      if (val) {
        used_row[r][val] = used_col[c][val] = used_mat[r / 3][c / 3][val] =
            true;
      }
    }
  }

  BT(0, 0);

  for (int i = 0; i < 9; ++i) {
    for (int j = 0; j < 9; ++j) {
      cout << ans[i][j];
    }
    cout << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}