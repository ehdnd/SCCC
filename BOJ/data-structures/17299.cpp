#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> A, ans, F, stk;

void Solve() {
  cin >> N;
  A.resize(N, 0);
  ans.resize(N, -1);
  F.resize(1010101, 0);

  for (int& num : A) {
    cin >> num;
    F[num]++;
  }

  for (int i = 0; i < N; ++i) {
    const int& num = A[i];

    while (!stk.empty() && F[A[stk.back()]] < F[num]) {
      ans[stk.back()] = num;
      stk.pop_back();
    }

    stk.push_back(i);
  }

  for (const int& num : ans) cout << num << " ";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}