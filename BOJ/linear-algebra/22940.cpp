#include <bits/stdc++.h>
using namespace std;

int N;
vector<vector<double>> matrix;
vector<double> result;

void GaussianElimination() {
  for (int i = 0; i < N; i++) {
    double pivot = matrix[i][i];
    for (int j = 1; j <= N; j++) matrix[i][j] /= pivot;

    // k 다른 행
    for (int k = 0; k < N; k++) {
      if (k == i) continue;
      double factor = matrix[k][i];
      for (int j = i; j <= N; j++) matrix[k][j] -= (factor * matrix[i][j]);
    }
  }

  for (int i = N - 1; i >= 0; i--) {
    result[i] = matrix[i][N];
    for (int j = i + 1; j < N; j++) {
      result[i] -= matrix[i][j] * result[j];
    }
  }
}

void Solve() {
  cin >> N;
  matrix.resize(N, vector<double>(N + 1));
  result.resize(N);

  for (auto& row : matrix)
    for (auto& val : row) cin >> val;

  GaussianElimination();

  for (const auto& val : result) cout << val << " ";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}