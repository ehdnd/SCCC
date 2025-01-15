#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 1e9 + 7;
ll N;

struct Matrix {
  int size;
  vector<vector<ll>> data;

  Matrix(int size) : size(size), data(size, vector<ll>(size, 0)) {}

  Matrix operator*(const Matrix& other) const {
    Matrix result(this->size);

    for (int i = 0; i < size; i++) {
      for (int k = 0; k < size; k++) {
        for (int j = 0; j < size; j++) {
          result.data[i][k] += (data[i][j] * other.data[j][k]) % MOD;
          result.data[i][k] %= MOD;
        }
      }
    }
    return result;
  }
};

void Solve() {
  cin >> N;
  if (N == 0) {
    cout << 0 << "\n";
    return;
  }

  Matrix result(4);
  Matrix base(4);
  result.data[0][0] = result.data[1][1] = 1;
  base.data[0][0] = base.data[0][1] = base.data[1][0] = 1;

  N--;
  while (N) {
    if (N & 1) result = result * base;
    base = base * base;
    N >>= 1;
  }

  cout << result.data[0][0];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}