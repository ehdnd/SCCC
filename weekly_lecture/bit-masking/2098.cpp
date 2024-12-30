#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

const int INF = 1e9;
int N;
int W[16][16], dp[16][1 << 16];

bool isVisited(int visited, int next) { return visited & (1 << next); }

// TSP(현재 정점, 현재 정점 포함 방문 정점)
// -> 남은 정점 방문 순회 최단 거리
int TSP(int current, int visited) {
  int& ret = dp[current][visited];
  if (ret != -1) return ret;

  // basecase: 모든 정점 방문 == 모든 비트가 1
  if (visited == (1 << N) - 1) {
    // 시작점으로 이동 불가능
    if (W[current][0] == 0) return INF;
    return W[current][0];
  }

  ret = INF;
  for (int i = 0; i < N; i++) {
    // 다음 정점 이미 방문 or 이동 불가능
    if (isVisited(visited, i) || W[current][i] == 0) continue;
    int next_visited = visited | (1 << i);
    ret = min(ret, TSP(i, next_visited) + W[current][i]);
  }
  return ret;
}

void Solve() {
  cin >> N;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++) cin >> W[i][j];
  memset(dp, -1, sizeof(dp));
  cout << TSP(0, 1);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}