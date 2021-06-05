# runitplusplus

## description 
runitと似たような感じ
## solution

### 疑似コード

```
int main(int arg0) {
    ebp = &stack[-8];
    *(var_10h) = mmap(0x0, 0x400, 0x7, 0x22, 0x0, 0x0);
    alarm(0xa);
    setvbuf(*stdout@@GLIBC_2.0, 0x0, 0x2, 0x0);
    setvbuf(*__TMC_END__, 0x0, 0x2, 0x0);
    puts("Send me stuff!!");
    esp = (((((((esp & 0xfffffff0) - 0x40) + 0x20 - 0x10) + 0x10 - 0x10) + 0x10 - 0x10) + 0x10 - 0x10) + 0x10 - 0x10) + 0x10;
    var_ch = read(0x0, var_10h, 0x400);
    if (var_ch < 0x0) {
            puts("Error reading!");
            eax = exit(0x1);
    }
    else {
            var_14h = 0x0;
            do {
                    eax = (var_ch);
                    if (SAR(eax + (eax >> 0x1f), 0x1) <= *(ebp - 0x14)) {
                        break;
                    }
                    edx = *(ebp - 0x10);
                    eax = *(ebp - 0x14);
                    *(int8_t *)(eax + edx) = *(int8_t *)(*(ebp - 0x10) + (*(ebp - 0xc) - *(ebp - 0x14) - 0x1)) & 0xff ^ *(int8_t *)(*(ebp - 0x14) + *(ebp - 0x10)) & 0xff;
                    
                    ebx = *(int8_t *)(eax + edx) & 0xff;
                    edx = *(ebp - 0xc) - *(ebp - 0x14) - 0x1;
                    eax = *(ebp - 0x10);
                    *(int8_t *)(eax + edx) = *(int8_t *)(*(ebp - 0x10) + (*(ebp - 0xc) - *(ebp - 0x14) - 0x1)) & 0xff ^ ebx;
                    *(int8_t *)(*(ebp - 0x14) + *(ebp - 0x10)) = *(int8_t *)(*(ebp - 0x14) + *(ebp - 0x10)) & 0xff ^ *(int8_t *)(eax + edx) & 0xff;
                    *(ebp - 0x14) = *(ebp - 0x14) + 0x1;
            } while (true);
            (*(ebp - 0x10))();
            eax = 0x0;
    }
    return eax;

```

xorしている部分は実は要素の入れ替えをしている。
詳しくはxor交換アルゴリズムを参照
疑似コードを見てみると、文字列を逆順にしていて、それを実行しているので、
シェルコードを逆順にしたものをペイロードして送る