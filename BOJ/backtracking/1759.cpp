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

  string prev_password = password;
  int curr_c, curr_v;

  for (int i = idx; i < C; ++i) {
    curr_c = c_cnt, curr_v = v_cnt;

    const char alpha = alphas[i];

    if (vowels.count(alpha))
      curr_v++;
    else
      curr_c++;

    password += alpha;

    BT(password, i + 1, len + 1, curr_v, curr_c);

    password = prev_password;
  }
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