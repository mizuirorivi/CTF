#include <stdio.h>

int main()
{
    char v[8];
    long canary = ((long *)v)[1];
    printf("%016lx\n", canary);
}
