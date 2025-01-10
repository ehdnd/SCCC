#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matrix = vector<vector<int>>;

const int MOD = 1000;
int N;
ll B;
matrix base, res;

matrix operator*(const matrix& mat1, const matrix& mat2) {
  matrix result(N, vector<int>(N));

  for (int i = 0; i < N; i++) {
    for (int k = 0; k < N; k++) {
      for (int j = 0; j < N; j++) {
        result[i][k] += (mat1[i][j] * mat2[j][k]);
      }
      result[i][k] %= MOD;
    }
  }
  return result;
};

void MatrixPow(ll b) {
  while (b) {
    if (b & 1) res = res * base;
    base = base * base;
    b >>= 1;
  }
};

void Solve() {
  cin >> N >> B;

  base.resize(N, vector<int>(N, 0));
  res.resize(N, vector<int>(N, 0));

  for (int i = 0; i < N; i++) {
    res[i][i] = 1;  // 단위행렬
  }

  for (auto& row : base)
    for (auto& val : row) {
      int temp;
      cin >> temp;
      val = temp % MOD;
    }

  MatrixPow(B);

  for (const auto& row : res) {
    for (const auto& val : row) {
      cout << val << " ";
    }
    cout << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}