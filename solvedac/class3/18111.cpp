#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int N, M, B, ans_t, ans_h, max_h;
int ground[500 * 500];

void Solve() {
  cin >> N >> M >> B;
  for (int i = 0; i < N * M; ++i) {
    cin >> ground[i];
    max_h = max(max_h, ground[i]);
  };

  max_h = min(max_h, 256);
  ans_t = INF;

  for (int curr_h = max_h; curr_h >= 0; --curr_h) {
    int t = 0;
    int inven = B;

    for (int i = 0; i < N * M; ++i) {
      const int& val = ground[i];
      int need_blocks = abs(curr_h - val);

      if (curr_h > val) {
        inven -= need_blocks;
        t += need_blocks;
      } else if (curr_h < val) {
        inven += need_blocks;
        t += need_blocks * 2;
      }
    }

    if (inven >= 0) {
      if (t < ans_t) {
        ans_t = t;
        ans_h = curr_h;
      }
    }
  }

  cout << ans_t << " " << ans_h;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}