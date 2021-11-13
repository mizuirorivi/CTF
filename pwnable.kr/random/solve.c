#include<stdio.h>

int main(){
    unsigned int random;
    random = rand();
    printf("answer = %d\n",random^0xdeadbeef);
}