#include <bits/stdc++.h>
using namespace std;

string A, B;
int M;

void Solve() {
  cin >> A >> M;

  while (M--) {
    string q;
    cin >> q;

    if (q == "L") {
      if (!A.empty()) {
        B.push_back(A.back());
        A.pop_back();
      }
    } else if (q == "D") {
      if (!B.empty()) {
        A.push_back(B.back());
        B.pop_back();
      }
    } else if (q == "B") {
      if (!A.empty()) A.pop_back();
    } else if (q == "P") {
      char x;
      cin >> x;
      A.push_back(x);
    }
  }

  while (!B.empty()) {
    A.push_back(B.back());
    B.pop_back();
  }

  cout << A << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}