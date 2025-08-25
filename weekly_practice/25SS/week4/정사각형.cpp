#include <bits/stdc++.h>
#define x first
#define y second
using namespace std;
using pii = pair<int, int>;

struct pair_hash {
  size_t operator()(const pii& p) const {
    return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
  }
};

void Solve() {
  int N;
  cin >> N;

  unordered_set<pii, pair_hash> pset;
  vector<pii> pts;

  for (int i = 0; i < N; ++i) {
    pii p;
    cin >> p.x >> p.y;
    pset.insert(p);
    pts.push_back(p);
  }

  int ans = 0;

  for (int i = 0; i < N; ++i) {
    for (int j = i + 1; j < N; ++j) {
      const pii& a = pts[i];
      const pii& b = pts[j];

      int dx = a.x - b.x;
      int dy = a.y - b.y;

      pii c1 = {a.x + dy, a.y - dx};
      pii d1 = {b.x + dy, b.y - dx};

      if (pset.count(c1) && pset.count(d1)) {
        ans = max(ans, dx * dx + dy * dy);
      }
    }
  }

  cout << ans << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}