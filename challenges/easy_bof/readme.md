# easy_bof

by JunGu Kang

## Description

### Description

This is not a hard one. But I think you need reverse-engineering skill.

### Notices

* No Notices

### Hints

#### 1st Hint

If you find proper key of given seed, you will reach vulnerable code. Seed is generated randomly.

### Files

* [easy_bof](https://github.com/ajou-whois/1st-cyber-security-mini-ctf/blob/master/challenges/easy_bof/easy_bof)

## Author's Comment

seed 값에 대한 적절한 key를 주면, `gets()`로 입력을 받는 취약한 코드가 있습니다.
seed는 무작위로 생성되므로, 바이너리를 분석해서 임의의 seed에 대한 key를 생성하는 로직을 찾아야 합니다.

## ETC

### Environment

#### Compile Setting

```text
$ gcc easy_bof.c -o easy_bof -m32 -s -fno-stack-protector -mpreferred-stack-boundary=2
```

#### ETC

* No ASLR