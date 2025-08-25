#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

struct VectorHash {
  size_t operator()(const vector<int>& v) const {
    size_t seed = v.size();
    for (auto& i : v) {
      seed ^=
          hash<int>()(i) + 0x9e3779b97f4a7c15ULL + (seed << 6) + (seed >> 2);
    }
    return seed;
  }
};

int N, M;
vector<int> st, ed;
unordered_map<vector<int>, int, VectorHash> dist;
vector<tuple<int, int, int>> edges;

void Solve() {
  cin >> N;
  for (int i = 0; i < N; ++i) {
    int val;
    cin >> val;
    st.push_back(val);
    ed.push_back(val);
  }
  sort(all(ed));

  cin >> M;
  while (M--) {
    int a, b, c;
    cin >> a >> b >> c;
    edges.emplace_back(--a, --b, c);
  }

  priority_queue<pair<int, vector<int>>> pq;
  dist[st] = 0;
  pq.emplace(0, st);

  while (!pq.empty()) {
    auto [w, x] = pq.top();
    pq.pop();
    w *= -1;
    if (dist[x] < w) continue;

    for (const auto& [a, b, d] : edges) {
      vector<int> nx = x;
      swap(nx[a], nx[b]);

      if (dist.count(nx) && dist[nx] <= dist[x] + d) continue;
      dist[nx] = dist[x] + d;
      pq.emplace(-dist[nx], nx);
    }
  }

  cout << (dist.count(ed) ? dist[ed] : -1);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}