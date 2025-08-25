#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

const int INF = 2e9 + 1;

int N;
vector<int> pos, neg;

void Solve() {
  cin >> N;
  while (N--) {
    int val;
    cin >> val;
    (val < 0) ? neg.push_back(val) : pos.push_back(val);
  }

  sort(all(neg), greater<int>());
  sort(all(pos));

  if (neg.empty()) {
    cout << pos[0] << " " << pos[1];
    return;
  }
  if (pos.empty()) {
    cout << neg[1] << " " << neg[0];
    return;
  }

  int min_diff = INF;
  int a, b;

  for (const auto& n_val : neg) {
    int idx = upper_bound(all(pos), -n_val) - pos.begin();

    int curr_diff, temp_b;

    if (idx == 0) {
      curr_diff = abs(n_val + pos[idx]);
      temp_b = pos[idx];
    } else if (idx == pos.size()) {
      curr_diff = abs(n_val + pos[idx - 1]);
      temp_b = pos[idx - 1];
    } else {
      int tf = abs(n_val + pos[idx - 1]);
      int ts = abs(n_val + pos[idx]);

      if (tf < ts) {
        curr_diff = tf;
        temp_b = pos[idx - 1];
      } else {
        curr_diff = ts;
        temp_b = pos[idx];
      }
    }

    if (curr_diff < min_diff) {
      min_diff = curr_diff;
      a = n_val;
      b = temp_b;
    }

    if (pos.size() >= 2) {
      int sum = pos[0] + pos[1];
      if (sum < min_diff) {
        min_diff = sum;
        a = pos[0];
        b = pos[1];
      }
    }

    if (neg.size() >= 2) {
      int sum = abs(neg[0] + neg[1]);
      if (sum < min_diff) {
        min_diff = sum;
        a = neg[0];
        b = neg[1];
      }
    }
  }

  if (a > b) swap(a, b);
  cout << a << " " << b;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}

// 투포인터로 풀자..
// -99 -98 1 0 96