#include <stdio.h>
#include <pthread.h>

void *print_ssp(void *a)
{
    char v[8];
    long canary = ((long *)v)[1];
    printf("%016lx\n", canary);
}

void *thread_main(void *a)
{
    print_ssp(NULL);
}

int main()
{
    print_ssp(NULL);
    for (int i=0; i<10; i++)
    {
        pthread_t h;
        pthread_create(&h, NULL, thread_main, NULL);
    }
    for(;;);
}
