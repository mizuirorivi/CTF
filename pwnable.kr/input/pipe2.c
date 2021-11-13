#include<stdio.h>
#include<signal.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>

#define READ (0)
#define WRITE (1)

/**
 * @param *fd_r read_fd 
 * @param *fd_w write_fd 
 * 
 *
*/
int popen2(int *fd_r,int *fd_w){
    /* 子から親への通信パイプ */
    int pipe_chile2parent[2];
    /* 親から子への通信用パイプ */
    int pipe_parent2child[2];

    /* プロセスID */
    int pid;
    if(pipe(pipe_chile2parent) < 0){
        /* パイプ生成失敗 */
        perror("popen2");
        return 1;
    }

    /* パイプを生成 */
    if(pipe(pipe_parent2child) < 0){
        /* パイプ生成失敗 */
        perror("popen2");

        /* 上で開いたパイプを閉じてから終了 */
        close(pipe_chile2parent[READ]);
        close(pipe_chile2parent[WRITE]);
        return 1;
    }

    /* fork */
    if((pid = fork()) < 0){
        /* fork失敗 */
        perror("popen2");

        /* 開いたパイプを閉じる */
        close(pipe_chile2parent[READ]);
        close(pipe_chile2parent[WRITE]);

        close(pipe_parent2child[READ]);
        close(pipe_parent2child[WRITE]);
        
        return 1;
    }
}

int main(int argc,char *argv[]){
    int fd_r = fileno(stdin);
    int fd_w = fileno(stdout);

    if(argc < 2){
        printf("Usage: %s <message>\n",argv[0]);
        return 1;
    }

    popen2(&fd_r,&fd_w);
    write(fd_w,argv[1],strlen(argv[1]));

    char buf[256];
    int size = read(fd_r,buf,255);
    if(size == -1){
        perror("error");
        return 1;
    }
    printf("test2: ");
    fwrite(buf,1,size,stdout);
    printf("\n");

    return 0;
}