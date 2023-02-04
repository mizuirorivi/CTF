# passcode

## Description

## Solution



sshしてみると,以下のようなc言語のファイルと実行ファイルが見える。

login()の中でpasscode1とpasscode2の入力をする時にpasscode1とpasscode2のアドレスではなく変数そのものを指定しているため、passcode1かpasscode2を任意の値にすることで値のアドレスの命令を書き換えられることがわかる。

```c
#include <stdio.h>
#include <stdlib.h>

void login(){
	int passcode1;
	int passcode2;

	printf("enter passcode1 : ");
	scanf("%d", passcode1);
	fflush(stdin);

	// ha! mommy told me that 32bit is vulnerable to bruteforcing :)
	printf("enter passcode2 : ");
        scanf("%d", passcode2);

	printf("checking...\n");
	if(passcode1==338150 && passcode2==13371337){
                printf("Login OK!\n");
                system("/bin/cat flag");
        }
        else{
                printf("Login Failed!\n");
		exit(0);
        }
}

void welcome(){
	char name[100];
	printf("enter you name : ");
	scanf("%100s", name);
	printf("Welcome %s!\n", name);
}

int main(){
	printf("Toddler's Secure Login System 1.0 beta.\n");

	welcome();
	login();

	// something after login...
	printf("Now I can safely trust you that you have credential :)\n");
	return 0;	
}


```



welcome()のなかでname[100]を入力しているが、ここのnameとpasscode1が被っている。

なので適当にpasscode1を任意の値に書き換えてGOT-overwriteすればよし