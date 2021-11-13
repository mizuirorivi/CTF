# RANDOM
## DESCRIPTION
> Daddy, teach me how to use random value in programming!

ssh random@pwnable.kr -p2222 (pw:guest)
## SOLUTION

cのrand()は毎回同じやつが出力される。
比較にxorを使っているのでrand() ^ 0xdeadbeefで計算された値が求める値となる