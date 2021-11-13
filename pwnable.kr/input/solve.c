#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
int main()
{
    char *args[101] = {};
    //argv 
    for (int i = 0; i < 101; i++)
    {
        args[i] = "A";
    }
    args['A'] = "\x00";
    args['B'] = "\x20\x0a\x0d";
    args[100] = NULL;
    printf("%x", args['A']);
    // stdio
    open('./mystdin',O_WRONLY);
    write('./mystdin',"\x00\x0a\x00\xff", 4);
    
    execve("/home/mizuiro/PROJECTS/security/ctf/pwnable.kr/input/input", args, NULL);
}
