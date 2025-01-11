#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

string n1, n2, result;
int carry, sum, len1, len2, len_max;

void Solve() {
  cin >> n1 >> n2;

  len1 = n1.length();
  len2 = n2.length();
  len_max = max(len1, len2);

  n1 = string(len_max - len1, '0') + n1;
  n2 = string(len_max - len2, '0') + n2;

  for (int i = len_max - 1; i >= 0; i--) {
    sum = (n1[i] - '0') + (n2[i] - '0') + carry;
    carry = sum / 10;
    result += ((sum % 10) + '0');
  }

  if (carry) result += (carry + '0');

  reverse(all(result));

  cout << result << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}