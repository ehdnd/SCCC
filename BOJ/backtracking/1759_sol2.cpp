#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int L, C;
vector<char> alphas;
unordered_set<char> vowels;

void BT(string password, int idx, int len, int v_cnt, int c_cnt) {
  if (len == L) {
    if (v_cnt >= 1 && c_cnt >= 2) {
      cout << password << "\n";
    }
    return;
  }
  if (idx == C) return;

  const char alpha = alphas[idx];
  if (vowels.count(alpha))
    BT(password + alpha, idx + 1, len + 1, v_cnt + 1, c_cnt);
  else
    BT(password + alpha, idx + 1, len + 1, v_cnt, c_cnt + 1);

  BT(password, idx + 1, len, v_cnt, c_cnt);
}

void Solve() {
  cin >> L >> C;
  alphas.resize(C);
  for (char& c : alphas) cin >> c;

  sort(all(alphas));

  vowels = {'a', 'e', 'i', 'o', 'u'};

  BT("", 0, 0, 0, 0);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}