# easy_crypto

by JuSung Ko

## Description

### Description

다음 암호화 소스코드를 분석한 후, 주어진 암호문들 중 숨겨진 flag를 찾으시오.

### Notices

* No Notices

### Hints

#### 1st Hint

* `c` 파일 : C언어 암호화 소스코드
* `Ciphers.txt` 파일 : 소스코드를 이용해 암호화한 결과들을 모아둔 파일
* `[Cipher 000]` -> Cipher num
* `9dbd74c7e7d461d2d16481ab2395b995013cedce95bd4e6ef397b568c2ac2ca8a70fb3c78c1dd0c0` -> Encryption Result

### Files

* [source.c](https://github.com/ajou-whois/1st-cyber-security-mini-ctf/blob/master/challenges/easy_crypto/source.c)
* [ciphers.txt](https://github.com/ajou-whois/1st-cyber-security-mini-ctf/blob/master/challenges/easy_crypto/ciphers.txt)

## Author's Comment

소스코드를 분석하면 평문과 같은 길이의 랜덤 수열을 키로 사용하는 것을 알 수 있습니다.
하지만 출력부분을 살펴보면 암호화에 이용한 키는 암호문과 함께 출력되는 것을 알 수 있습니다.

## ETC
