# runit - BSidesSF 2019 CTF

## Description

```
$ checksec runit 
emac[*] 'runit'
    Arch:       32 bits (little endian)
    NX:         NX enabled
    SSP:        SSP disabled (No canary found)
    RELRO:      Partial RELRO
    PIE:        PIE disabled
```
シェルコードを送ると実行してくれるバイナリだった。

## Solution

