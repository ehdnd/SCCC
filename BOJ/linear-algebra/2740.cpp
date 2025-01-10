#include <bits/stdc++.h>
using namespace std;

int N, M, K;
int A[101][101], B[101][101], C[101][101];

void Solve() {
  cin >> N >> M;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < M; j++) cin >> A[i][j];

  cin >> M >> K;
  for (int i = 0; i < M; i++)
    for (int j = 0; j < K; j++) cin >> B[i][j];

  for (int i = 0; i < N; i++) {
    for (int k = 0; k < K; k++) {
      for (int j = 0; j < M; j++) {
        C[i][k] += (A[i][j] * B[j][k]);
      }
    }
  }

  for (int i = 0; i < N; i++) {
    for (int k = 0; k < K; k++) {
      cout << C[i][k] << " ";
    }
    cout << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}