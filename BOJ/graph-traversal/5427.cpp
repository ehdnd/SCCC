#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

int W, H;
int G[1010][1010];
int fire_vis[1010][1010];
int sang_vis[1010][1010];

int dh[4] = {1, -1, 0, 0};
int dw[4] = {0, 0, 1, -1};

inline bool CheckBound(int h, int w) {
  return 0 <= h && h < H && 0 <= w && w < W;
}

void Initialize() {
  memset(G, 0, sizeof(G));
  memset(fire_vis, 0, sizeof(fire_vis));
  memset(sang_vis, 0, sizeof(sang_vis));
}

void FireBfs(queue<pii>& q) {
  int q_size = q.size();

  while (q_size--) {
    auto [h, w] = q.front();
    q.pop();

    for (int i = 0; i < 4; i++) {
      int nh = h + dh[i];
      int nw = w + dw[i];

      if (!CheckBound(nh, nw) || fire_vis[nh][nw] || G[nh][nw]) continue;

      fire_vis[nh][nw] = 1;
      q.emplace(nh, nw);
    }
  }
}

int SangBfs(queue<pii>& q) {
  int q_size = q.size();

  if (q_size == 0) return -1;

  while (q_size--) {
    auto [h, w] = q.front();
    q.pop();

    for (int i = 0; i < 4; i++) {
      int nh = h + dh[i];
      int nw = w + dw[i];

      if (!CheckBound(nh, nw)) return 1;

      if (fire_vis[nh][nw] || sang_vis[nh][nw] || G[nh][nw]) continue;

      sang_vis[nh][nw] = 1;
      q.emplace(nh, nw);
    }
  }
  return 0;
}

void Solve() {
  cin >> W >> H;
  Initialize();

  queue<pii> fire_q, sang_q;

  for (int h = 0; h < H; h++) {
    for (int w = 0; w < W; w++) {
      char c;
      cin >> c;
      switch (c) {
        case '.':
          G[h][w] = 0;
          break;
        case '#':
          G[h][w] = 1;
          break;
        case '@':
          sang_q.emplace(h, w);
          sang_vis[h][w] = 1;
          break;
        case '*':
          fire_q.emplace(h, w);
          fire_vis[h][w] = 1;
          break;
        default:
          break;
      }
    }
  }

  int cnt = 0;
  while (1) {
    cnt++;

    FireBfs(fire_q);
    int sts = SangBfs(sang_q);

    if (sts == -1) {
      cout << "IMPOSSIBLE" << "\n";
      return;
    } else if (sts == 1) {
      cout << cnt << "\n";
      return;
    }
  }

  cout << "IMPOSSIBLE" << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}