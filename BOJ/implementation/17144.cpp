#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int R, C, T;
int A[50][50];
int temp[50][50];
int air_top, air_bot;

int dr[4] = {1, -1, 0, 0};
int dc[4] = {0, 0, 1, -1};

inline bool inRange(int r, int c) { return 0 <= r && r < R && 0 <= c && c < C; }

void Input() {
  cin >> R >> C >> T;

  for (int r = 0; r < R; r++) {
    for (int c = 0; c < C; c++) {
      cin >> A[r][c];
      if (A[r][c] == -1) {
        if (!air_top && !air_bot) {
          air_top = r;
        } else {
          air_bot = r;
        }
      }
    }
  }
}

void SpreadDustNow(int r, int c) {
  int amount = A[r][c];
  int spread_amount = amount / 5;

  if (spread_amount == 0) {
    temp[r][c] += amount;
    return;
  }

  int cnt_spread = 0;
  for (int i = 0; i < 4; i++) {
    int nr = r + dr[i];
    int nc = c + dc[i];

    if (!inRange(nr, nc) || A[nr][nc] == -1) continue;

    temp[nr][nc] += spread_amount;
    cnt_spread++;
  }

  temp[r][c] += (amount - spread_amount * cnt_spread);
}

void SpreadDust() {
  memset(temp, 0, sizeof(temp));
  temp[air_top][0] = temp[air_bot][0] = -1;

  for (int r = 0; r < R; r++) {
    for (int c = 0; c < C; c++) {
      if (A[r][c] > 0) SpreadDustNow(r, c);
    }
  }

  swap(A, temp);
}

void OperateCleaner() {
  for (int r = air_top - 1; r > 0; r--) A[r][0] = A[r - 1][0];
  for (int c = 0; c < C - 1; c++) A[0][c] = A[0][c + 1];
  for (int r = 0; r < air_top; r++) A[r][C - 1] = A[r + 1][C - 1];
  for (int c = C - 1; c > 1; c--) A[air_top][c] = A[air_top][c - 1];
  A[air_top][1] = 0;

  for (int r = air_bot + 1; r < R - 1; r++) A[r][0] = A[r + 1][0];
  for (int c = 0; c < C - 1; c++) A[R - 1][c] = A[R - 1][c + 1];
  for (int r = R - 1; r > air_bot; r--) A[r][C - 1] = A[r - 1][C - 1];
  for (int c = C - 1; c > 1; c--) A[air_bot][c] = A[air_bot][c - 1];
  A[air_bot][1] = 0;
}

void Solve() {
  Input();

  while (T--) {
    SpreadDust();
    OperateCleaner();
  }

  ll res = 0;
  for (int r = 0; r < R; r++)
    for (int c = 0; c < C; c++)
      if (A[r][c] > 0) res += A[r][c];

  cout << res;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}