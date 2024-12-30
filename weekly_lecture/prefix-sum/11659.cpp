#include <bits/stdc++.h>
using namespace std;

int N, M;
int prefix_sum[101010];

// 입력 받으면서 제작
void MakePrefixSum() {
  for (int i = 0; i < N; i++) {
    int a;
    cin >> a;
    prefix_sum[i + 1] = prefix_sum[i] + a;
  };
}

void Solve() {
  cin >> N >> M;
  MakePrefixSum();
  for (int i = 0; i < M; i++) {
    int s, e;
    cin >> s >> e;
    // 배열 인덱스 주의
    cout << prefix_sum[e] - prefix_sum[s - 1] << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}