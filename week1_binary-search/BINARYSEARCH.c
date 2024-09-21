#include <stdio.h>

int binSearch(int arr[], int len, int x) {
  // initialization
  int left = 0;
  int right = len - 1;
  int mid;

  while (left <= right) {
    mid = left + (right - left) / 2;

    if (x == arr[mid]) {
      return mid;
    } else if (x < arr[mid]) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return -1;
}
