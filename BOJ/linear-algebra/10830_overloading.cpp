#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 1000;
int N;
ll B;

struct Matrix {
  int size;
  vector<vector<int>> data;

  Matrix(int size) : size(size), data(size, vector<int>(size, 0)) {}

  Matrix operator*(const Matrix& other) const {
    Matrix result(N);

    for (int i = 0; i < N; i++) {
      for (int k = 0; k < N; k++) {
        for (int j = 0; j < N; j++) {
          result.data[i][k] += (data[i][j] * other.data[j][k]) % MOD;
          result.data[i][k] %= MOD;
        }
      }
    }
    return result;
  }

  Matrix& operator*=(const Matrix& other) {
    *this = *this * other;
    return *this;
  }

  friend ostream& operator<<(ostream& os, const Matrix& mat) {
    for (const auto& row : mat.data) {
      for (const auto& val : row) {
        os << val << " ";
      }
      os << "\n";
    }
    return os;
  }
};

void MatrixPow(ll b, Matrix& base, Matrix& res) {
  while (b) {
    if (b & 1) res *= base;
    base *= base;
    b >>= 1;
  }
};

void Solve() {
  cin >> N >> B;

  Matrix base(N);
  Matrix res(N);

  for (int i = 0; i < N; i++) res.data[i][i] = 1;

  for (auto& row : base.data)
    for (auto& val : row) cin >> val;

  MatrixPow(B, base, res);

  cout << res;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}