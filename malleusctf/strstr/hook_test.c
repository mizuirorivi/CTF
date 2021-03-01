#include <stdio.h>
#include <malloc.h>

void *my_malloc(size_t size, const void *caller)
{
    printf("malloc(%zu)\n", size);
}

void my_free(void *ptr, const void *caller)
{
    printf("free(\"%s\")\n", (const char *)ptr);
}

int main()
{
    //  printfの初回呼び出し時にmallocが呼ばれる
    //  my_malloc中の呼び出しが初回呼び出しだとエラーになるので、
    //  あらかじめ呼び出しておく
    printf("aaaa\n");

    __malloc_hook = my_malloc;
    __free_hook = my_free;
    malloc(1234);
    free("test");
}
