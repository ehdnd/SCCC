#include <bits/stdc++.h>
using namespace std;

int N, M;
unordered_set<int> cards;

void Solve() {
  cin >> N;
  while (N--) {
    int card;
    cin >> card;
    cards.insert(card);
  }

  cin >> M;
  while (M--) {
    int query;
    cin >> query;
    cout << (cards.count(query) ? 1 : 0) << " ";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}