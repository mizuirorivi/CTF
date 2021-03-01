#include <stdio.h>

int main()
{
    long a = 0xdeadbeef;
    printf("1: %lx, 2: %lx, 3: %lx, 4: %lx\n"
           "5: %lx, 6: %lx, 7: %lx, 8: %lx\n");
    printf("7: %7$x\n");
}
