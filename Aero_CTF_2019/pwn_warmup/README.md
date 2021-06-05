# PWN_WARMUP
## Description
パスワードを入力しろ系の実行ファイルが渡される

## Solution

### 疑似コード
``` 
void main(){
    string var_29h;
    int var_9h;

    print("Memes server");
    print("Enter the password:");
    eax = read(0,var_29h,20h); // eax は文字数
    *(ebp+eax+(ebp-0x29)) = 0;
    auth(eax);

}

void auth(arg_0){
    
    var_Ch = malloc(0x40);
    readPassword(var_Ch);
    strcmp(arg_0,var_Ch);
}

void readPassword(){
    int32 var_Ch;
    var_Ch = fopen('password.txt',r);
}
```