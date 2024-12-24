#include <bits/stdc++.h>
using namespace std;

int N, A, B, M;
vector<int> graph[101];
int visited[101];

void Bfs(int st) {
  queue<int> q;
  q.push(st);
  visited[st] = 0;

  while (!q.empty()) {
    int v = q.front();
    q.pop();
    for (auto nx : graph[v]) {
      if (visited[nx] != -1) continue;
      visited[nx] = visited[v] + 1;
      q.push(nx);
    }
  }
}

void Solve() {
  cin >> N;
  cin >> A >> B;
  cin >> M;
  for (int i = 0; i < M; i++) {
    int a, b;
    cin >> a >> b;
    graph[a].push_back(b);
    graph[b].push_back(a);
  }
  for (int i = 1; i <= N; i++) visited[i] = -1;
  Bfs(A);

  cout << visited[B];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}