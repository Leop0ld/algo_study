#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int getMax(int numArr[], int length);
float getAverage(float numArr2[], int length);

int main() {
  char numberStr[100];
  int loop, maxNum, i = 0;

  scanf("%d\n", &loop);
  scanf(" %[^\n]s", numberStr);

  char* p = strtok(numberStr, " ");
  int numberArr[loop];
  float resultArr[loop];

  while (p != NULL) {
    numberArr[i++] = atoi(p);
    p = strtok(NULL, " ");
  }

  maxNum = getMax(numberArr, loop);

  for(i = 0; i < loop; i++) {
    resultArr[i] = (float)numberArr[i] / (float)maxNum * 100.0;
  }

  printf("%.2f\n", getAverage(resultArr, loop));

  return 0;
}

int getMax(int numArr[], int length) {
  int i;
  int maxNum = numArr[0];

  for(i = 1; i < length; i++) {
    if(maxNum < numArr[i]) maxNum = numArr[i];
  }

  return maxNum;
}

float getAverage(float numArr2[], int length) {
  float sum = 0.0;
  int i;

  for(i = 0; i < length; i++) {
    sum += numArr2[i];
  }

  return (float)sum/length;
}
