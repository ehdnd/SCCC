#include <bits/stdc++.h>
using namespace std;

struct Day {
  int a, b;

  Day() : a(0), b(0) {}
  Day(int a, int b) : a(a), b(b) {}

  Day operator+(const Day& d) const;
};

Day Day::operator+(const Day& d) const {
  Day temp(a + d.a, b + d.b);
  return temp;
}

int D, K;
Day A[31];

void Solve() {
  cin >> D >> K;
  A[1] = Day(1, 0);
  A[2] = Day(0, 1);

  for (int i = 3; i <= D; i++) A[i] = A[i - 2] + A[i - 1];

  const auto& [a, b] = A[D];

  for (int i = 1; i <= K; i++) {
    for (int j = i; j <= K; j++) {
      if ((a * i) + (b * j) == K) {
        cout << i << "\n" << j;
        return;
      }
    }
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}