#include<stdio.h>
#include<iostream>
using namespace std;
#include <vector>

void disp(int image[][5], int size){
  for(int i=0; i<size;i++){
    for(int j=0; j<size;j++){
        printf("%3.4d ",image[i][j]);
    }
    printf("\n");
  }
}


void rotate_matrix( int image[][5], int size){

  int t;
  for(int i = 0 ;i < size/2; i++){
      for(int j=i; j< size-i-1 ; j++){
        t = image[i][j];
        //move left to top
        image[i][j] = image[size-j-1][i];
        //move down to left
        image[size-j-1][i] = image[size-i-1][size-j-1];
        //move right to down
        image[size-i-1][size-j-1] = image[j][size-i-1];
        //move top to right
        image[j][size-i-1] = t;
    }
  }
}

int main(){
  int image[5][5] = { {1,2,3,4,5} , {6,7,8,9,10} , {11,12,13,14,15} , {16,17,18,19,20},{21,22,23,24,25} };
  rotate_matrix(image,5);
  return 0;
}
