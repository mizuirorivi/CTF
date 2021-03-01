#include <stdio.h>

long a = 0xdeadbeef;

int main()
{
    long *p = &a;
    printf("%7$s");
}
