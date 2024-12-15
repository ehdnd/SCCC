#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
#define prs(v)  \
  sort(all(v)); \
  v.erase(unique(all(v)), v.end())
using namespace std;
using ll = long long;
using P = pair<ll, ll>;
const int N = 100'101;
const ll oo = 1e15;
vector<int> G[N];
void solve() {
  int n, m, k;
  cin >> n >> m >> k;
  // 가중치 받자
  vector<ll> A(n + 1);
  for (int s = 1; s <= n; s++) cin >> A[s];
  vector<P> edg;
  // 그래프 받자
  for (int s = 0; s < m; s++) {
    int u, v;
    cin >> u >> v;
    edg.push_back({u, v});
    G[u].push_back(v);
    G[v].push_back(u);
  }
  // 초반 탈락
  if (n == 2 && k == 1) {
    cout << "impossible\n";
    return;
  }

  // 다익스트라 두번번
  vector<ll> d1(n + 1, oo), d2(n + 1, oo);
  d1[1] = A[1];
  d2[n] = A[n];
  priority_queue<P> pq;
  pq.push({-d1[1], 1});
  while (pq.size()) {
    auto [d, v] = pq.top();
    pq.pop();
    if (d1[v] < -d) continue;
    for (int nx : G[v])
      if (d1[nx] > d1[v] + A[nx]) {
        d1[nx] = d1[v] + A[nx];
        pq.push({-d1[nx], nx});
      }
  }
  while (pq.size()) pq.pop();
  pq.push({-d2[n], n});
  while (pq.size()) {
    auto [d, v] = pq.top();
    pq.pop();
    if (d2[v] < -d) continue;
    for (int nx : G[v])
      if (d2[nx] > d2[v] + A[nx]) {
        d2[nx] = d2[v] + A[nx];
        pq.push({-d2[nx], nx});
      }
  }
  // 정점 순서 결정
  int cnt1 = 0, cnt2 = 0;
  vector<int> idg(n + 1), ord;
  auto sht = [&](int i) { return d1[i] + d2[i] - A[i] == d2[1]; };
  // 다익스트라 바탕으로 정점 결정
  // indegree 만 설정하면 dag 나오는구나
  for (auto [u, v] : edg) {
    if (sht(u) && sht(v)) {
      if (d1[u] > d1[v]) swap(u, v);
      idg[v]++;
    }
  }
  //   for (int i : idg) cout << i << " ";
  // 위상정렬 시작
  queue<int> q;
  for (int s = 1; s <= n; s++)
    if (sht(s) && !idg[s]) q.push(s);
  while (q.size()) {
    int v = q.front();
    q.pop();
    ord.push_back(v);
    for (int nx : G[v]) {
      if (sht(nx)) {
        if (!--idg[nx]) q.push(nx);
      }
    }
  }
  vector<int> ans(n + 1);
  if (k > n - k) {
    for (int i : ord) {
      if (k) ans[i] = 1, k--;
    }
    for (int s = 1; s <= n; s++)
      if (!ans[s] && k) ans[s] = 1, k--;
  } else {
    for (int s = 1; s <= n; s++) ans[s] = 1;
    int p = n - k;
    for (int i : ord) {
      if (p) ans[i] = 0, p--;
    }
    for (int s = 1; s <= n; s++)
      if (ans[s] && p) ans[s] = 0, p--;
  }
  for (int s = 1; s <= n; s++) cout << (ans[s] ? 'N' : 'S');
  cout << "\n";
}
int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T = 1;
  while (T--) solve();
}