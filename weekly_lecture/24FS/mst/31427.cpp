#include <bits/stdc++.h>

using namespace std;

int N, M, Q;
int S[101010];
char School[5] = {"A", "B", 'C', 'D', 'E'};
bool V[5];
vector<int> per;
vector<vector<char>> permutation;

int Find(int a) {
  if (S[a] < 0) return a;
  return S[a] = Find(S[a]);
}

bool Union(int a, int b) {
  a = Find(a);
  b = Find(b);
  if (a == b) return 0;
  if (S[a] > S[b]) swap(a, b);
  S[a] += S[b];
  S[b] = a;
  return 1;
}

int backtracking(int cnt) {
  if (cnt == 5) {
    permutation.push_back(per);
    return;
  }
  for (int i = 0; i < 5; i++) {
    if (V[i]) continue;
    V[i] = true;
    per.push_back(School[i]);
    backtracking(cnt + 1);
    per.pop_back();
    V[i] = false;
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  cin >> N >> M >> Q;

  while (Q--) {
    backtracking(0);
    cout << 1 << " ";
  }
}