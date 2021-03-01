int main()
{
    void (*rce)(int, int, int) = (void *)(0x7ffff7dc8000LL + 0xe6ce9);
    rce(0, 0, 0);
}
