#include <bits/stdc++.h>
using namespace std;

int N, M, Q;
vector<int> S, tanks, cnts[2];

int Find(int a) { return S[a] < 0 ? a : S[a] = Find(S[a]); }

bool Union(int a, int b) {
  a = Find(a), b = Find(b);
  if (a == b) return 0;
  if (S[a] > S[b]) swap(a, b);
  S[a] += S[b], S[b] = a;
  return 1;
}

void Solve() {
  cin >> N >> M >> Q;

  S.resize(N, -1);
  tanks.resize(N, 0);
  cnts[0].resize(N);
  cnts[1].resize(N);

  for (int& x : tanks) cin >> x;

  while (M--) {
    int a, b;
    cin >> a >> b;
    Union(--a, --b);
  }

  for (int i = 0; i < N; ++i) cnts[tanks[i]][Find(i)]++;

  while (Q--) {
    int q;
    cin >> q;
    q--;
    cout << (cnts[0][Find(q)] < cnts[1][Find(q)]) << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}