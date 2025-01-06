#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

struct Node {
  int x, y;

  Node() = default;

  bool operator<(const Node& d) const {
    if (x == d.x) return y < d.y;
    return x < d.x;
  }
};

int N;
vector<Node> nodes;

void Solve() {
  cin >> N;

  nodes.resize(N);

  for (int i = 0; i < N; i++) {
    auto& [x, y] = nodes[i];
    cin >> x >> y;
  }

  sort(all(nodes));

  for (const auto& [x, y] : nodes) cout << x << " " << y << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}