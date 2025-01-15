#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int N, M;
vector<int> A, B, ans;
unordered_map<int, int> A_idx, B_idx;

void Solve() {
  cin >> N;
  for (int i = 0; i < N; i++) {
    int a;
    cin >> a;
    A.push_back(a);
    A_idx[a] = i;
  }
  cin >> M;
  for (int i = 0; i < M; i++) {
    int b;
    cin >> b;
    B.push_back(b);
    B_idx[b] = i;
  }

  int max_idx_A = 0, max_idx_B = 0;

  while (1) {
    int max_val = 0;

    for (int i = max_idx_B + 1; i < M; i++) {
      int b = B[i];
      if (max_val < b && A_idx.find(b) != A_idx.end() && max_idx_A < A_idx[b]) {
        max_val = max(max_val, b);
      }
    }

    if (max_val == 0) {
      break;
    } else {
      max_idx_A = A_idx[max_val];
      max_idx_B = B_idx[max_val];
      ans.push_back(max_val);
    }
  }

  int K = ans.size();
  cout << K << "\n";
  if (K)
    for (const int& k : ans) cout << k << " ";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}