#include <stdio.h>
#include <stdlib.h>

__thread int tls;

int main()
{
    int stack;
    char *small;
    char *large;
    small = (char *)malloc(1);
    large = (char *)malloc(0x21000);
    printf("main:   %p\n", main);
    printf("small:  %p\n", small);
    printf("large:  %p\n", large);
    printf("printf: %p\n", printf);
    printf("tls:    %p\n", &tls);
    printf("stack:  %p\n", &stack);
}
