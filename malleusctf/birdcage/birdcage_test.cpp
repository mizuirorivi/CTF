#include <cstdio>
#include <string>
using namespace std;

int main()
{
    string *p1, *p2, *p3;
    p1 = new string;
    p2 = new string;
    delete p1;
    p3 = new string;

    printf("p1: %p\n", p1);
    printf("p2: %p\n", p2);
    printf("p3: %p\n", p3);
    printf("sizeof(string): %zx\n", sizeof(string));
    printf("p2->size: %lx\n", ((long *)p2)[-1]);
    printf("p2->_M_p: %lx\n", ((long *)p2)[0]);
}
