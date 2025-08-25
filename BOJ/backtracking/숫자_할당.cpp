#include <bits/stdc++.h>
using namespace std;

int board[5][5], row_sum[5], col_sum[5];
bool used[14];
int cnt;

bool isPoss(int r, int c, int val) {
  if (used[val]) return false;

  const int& row_max = board[r][0];
  const int& col_max = board[0][c];

  if (row_max < row_sum[r] + val) return false;
  if (col_max < col_sum[c] + val) return false;

  if (row_max > row_sum[r] + val + (c - 1) * 13) return false;
  if (col_max > col_sum[c] + val + (r - 1) * 13) return false;

  return true;
}

void BT(int r, int c) {
  if (r == 0) {
    cnt++;
    return;
  }

  if (c == 0) {
    BT(r - 1, 4);
    return;
  }
  if (board[r][c] == 0) {
    BT(r, c - 1);
    return;
  }

  for (int i = 1; i <= 13; ++i) {
    if (!isPoss(r, c, i)) continue;

    used[i] = 1;
    board[r][c] = i;
    row_sum[r] += i;
    col_sum[c] += i;

    BT(r, c - 1);

    used[i] = 0;
    board[r][c] = -1;
    row_sum[r] -= i;
    col_sum[c] -= i;
  }
}

void Solve() {
  memset(board, -1, sizeof(board));

  for (int col = 1; col < 5; col++) cin >> board[0][col];
  for (int row = 1; row < 5; row++) cin >> board[row][0];

  board[0][0] = board[3][4] = board[4][3] = board[4][4] = 0;

  BT(4, 4);

  cout << cnt;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}