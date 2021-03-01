#include <stdio.h>

int main()
{
    int x, y;
    printf("abc%n%d%n\n", &x, 1234, &y);
    printf("x: %d, y: %d\n", x, y);
}
