#include <bits/stdc++.h>
using namespace std;

void Solve() {
  int N;
  double sum = 0;
  cin >> N;
  for (int i = 0; i < N; ++i) {
    string x;
    cin >> x;
    for (char& c : x) {
      if (c == '0' or c == '6') c = '9';
    }
    sum += min(stoi(x), 100);
  }

  cout << round(sum / N);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}