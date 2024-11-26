#include <bits/stdc++.h>

using namespace std;

int A[10101];
int S[10101];

int Find(int a) {
  if (S[a] < 0) return a;
  return S[a] = Find(S[a]);
}

bool Union(int a, int b) {
  a = Find(a);
  b = Find(b);
  if (a == b) return 0;
  if (A[a] > A[b]) swap(a, b);
  S[a] += S[b];
  S[b] = a;
  return 1;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int N, M, K, i;
  cin >> N >> M >> K;
  for (i = 1; i <= N; i++) {
    cin >> A[i];
    S[i] = -1;
  }
  for (i = 0; i < M; i++) {
    int v, w;
    cin >> v >> w;
    Union(v, w);
  }
  int res = 0;
  for (i = 1; i <= N; i++)
    if (S[i] < 0) res += A[i];
  if (res <= K)
    cout << res;
  else
    cout << "Oh no";
}