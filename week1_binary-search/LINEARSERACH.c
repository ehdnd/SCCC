#include <stdio.h>

int linSearch(int arr[], int len, int x) {
  int i;
  for (i = 0, i < len; i++) {
    if (arr[i] == x) {
      return i;
    }
  }
  return -1;
}