#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int M, S;
string query;

void add(int x) { S |= (1 << (x - 1)); }
void remove(int x) { S &= ~(1 << (x - 1)); }
// bool.. 0이면 false 아닌 모든 값은 true 반환
bool check(int x) { return S & (1 << (x - 1)); }
void toggle(int x) {
  if (check(x))
    remove(x);
  else
    add(x);
}
void all() { S = (1 << 20) - 1; }
void empty() { S = 0; }

void Solve() {
  cin >> M;
  for (int i = 0; i < M; i++) {
    cin >> query;
    int x;
    if (query == "add") {
      cin >> x;
      add(x);
    } else if (query == "remove") {
      cin >> x;
      remove(x);
    } else if (query == "check") {
      cin >> x;
      cout << check(x) << "\n";
    } else if (query == "toggle") {
      cin >> x;
      toggle(x);
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