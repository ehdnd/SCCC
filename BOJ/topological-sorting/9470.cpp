#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int K, M, P;
int idg[1010];
int strahlers[1010][2];
vector<int> graph[1010];

void Solve() {
  cin >> K >> M >> P;

  memset(idg, 0, sizeof(idg));
  memset(graph, 0, sizeof(graph));
  memset(strahlers, 0, sizeof(strahlers));

  for (int i = 0; i < P; i++) {
    int st, ed;
    cin >> st >> ed;
    graph[st].push_back(ed);
    idg[ed]++;
  }

  queue<int> Q;
  for (int i = 1; i <= M; i++) {
    if (!idg[i]) {
      Q.push(i);
      strahlers[i][0] = 1;
    }
  }

  while (!Q.empty()) {
    int v = Q.front();
    Q.pop();

    for (auto& nx : graph[v]) {
      const auto& [curr_max, curr_cnt] = strahlers[v];
      auto& [next_max, next_cnt] = strahlers[nx];

      if (next_max < curr_max) {
        next_max = curr_max;
        next_cnt = 1;
      } else if (next_max == curr_max) {
        if (next_cnt == -1)
          next_cnt = 1;
        else if (++next_cnt >= 2) {
          next_max++;
          next_cnt = -1;
        };
      }

      if (!--idg[nx]) Q.push(nx);
    }
  }
  cout << K << " " << strahlers[M][0] << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}