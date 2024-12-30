#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int M, S;
string query;

void add(int x) { S |= (1 << x); }
void remove(int x) { S &= ~(1 << x); }
bool check(int x) { return (S & (1 << x)) != 0; }
void toggle(int x) { S ^= (1 << x); }
void all() { S = (1 << 20) - 1; }
void empty() { S = 0; }

void Solve() {
  cin >> M;
  for (int i = 0; i < M; i++) {
    cin >> query;
    int x;
    if (query == "add") {
      cin >> x;
      add(x - 1);
    } else if (query == "remove") {
      cin >> x;
      remove(x - 1);
    } else if (query == "check") {
      cin >> x;
      cout << check(x - 1) << "\n";
    } else if (query == "toggle") {
      cin >> x;
      toggle(x - 1);
    } else if (query == "all") {
      all();
    } else {
      empty();
    }
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}