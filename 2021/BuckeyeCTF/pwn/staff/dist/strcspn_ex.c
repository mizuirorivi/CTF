#include <stdio.h>
#include <string.h>
#define  BUFFER_SIZE 300
int main(void)
{
    char buf[BUFFER_SIZE];
    printf("Enter the data = ");
    if (fgets(buf, sizeof(buf), stdin) == NULL)
    {
        printf("Fail to read the input stream");
    }
    else
    {
        buf[strcspn(buf, "\n")] = '\0';
    }
    printf("Entered Data = %s\n",buf);
    return 0;
}