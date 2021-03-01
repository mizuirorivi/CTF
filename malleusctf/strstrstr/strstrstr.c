 1: //  gcc strstrstr.c -o strstrstr -fpie -fcf-protection=none
 2: #include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void setup()
{
    alarm(60);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int read_index() {
    int index = 0;
    for (;;) {
        printf("index: ");
        scanf("%d", &index);
        if (0<=index && index<16)
            break;
        printf("invalid index\n");
    }
    return index;
}

int main()
{
    char *storage[16] = {};
    int command = 0;
    int index = 0;
    char buf[0x100];

    setup();

36:     printf(
37:         "<+><+><+> Strong String Storage <+><+><+>\n"
38:         "  0: store\n"
39:         "  1: show\n"
40:         "  2: delete\n"
41:         "  3: exit\n"
42:     );

    for (;;) {
        printf("command: ");
        scanf("%d", &command);

        switch (command) {
        case 0:
            index = read_index();
            printf("string: ");
            scanf("%255s", buf);
            storage[index] = (char *)malloc(strlen(buf));
            strcpy(storage[index], buf);
            break;
        case 1:
            index = read_index();
            puts(storage[index]);
            break;
60:         case 2:
61:             index = read_index();
62:             free(storage[index]);
63:             storage[index] = NULL;
64:             break;
        case 3:
            exit(0);
        default:
            printf("invalid command\n");
        }
    }
}
