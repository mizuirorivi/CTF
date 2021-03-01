#include <stdio.h>

char secret[] = "FLAG{secret}";

int main()
{
    puts("hi.");

    //  何らかの脆弱性で書き換えることができたと仮定
    stdout->_IO_read_end = secret;
    stdout->_IO_write_base = secret;
    stdout->_IO_write_ptr = secret+12;
    stdout->_IO_write_end = secret+12;

    puts("bye.");
}
