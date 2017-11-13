#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

#define MAX_LEN 1000
#define MIN_LEN 1

void keyGen(unsigned char*, int);

void main()
{
	char PlainText[MAX_LEN + 1];
	char inputKey[MAX_LEN + 1];
	unsigned char EncKey[MAX_LEN + 1];
	unsigned char CipherText[MAX_LEN + 1];

	printf("+------------------------------------------------------------------+\n");
	printf("|           This code is for 1st cyber security mini CTF           |\n");
	printf("|           This code doesn't have any malicious code              |\n");
	printf("|           Input is Plaintext(String)                             |\n");
	printf("|           Output is Ciphertext(Hex)                              |\n");
	printf("|           If you want to terminate this, press Enter Key only    |\n");
	printf("+------------------------------------------------------------------+\n\n");

	while (1) {
		memset(PlainText, 0x00, MAX_LEN + 1);
		memset(inputKey, 0x00, MAX_LEN + 1);
		memset(EncKey, 0x00, MAX_LEN + 1);
		memset(CipherText, 0x00, MAX_LEN + 1);

		printf("> Enter the Plain Text to Encrypt(MAX LENGTH : %d)\n> ", MAX_LEN);
		gets_s(PlainText, MAX_LEN + 1);

		if (strlen(PlainText) < MIN_LEN) {
			printf("> Enter the Valid Value\n\n");
			return;
		}

		keyGen(EncKey, strlen(PlainText));

		for (int i = strlen(PlainText) - 1; i >= 0; i--) {
			printf("%02x", EncKey[i]);
		}
		
		for (int i = 0; i < strlen(PlainText); i++) {
			CipherText[i] = PlainText[i] ^ EncKey[i];
			printf("%02x", CipherText[i]);

		}
		printf("\n\n");
	}
	printf("Terminated..\n");

	return;
}

void keyGen(unsigned char* EncKey, int size)
{
	srand(time(NULL));
	for (int i = 0; i < size; i++) {
		EncKey[i] = rand() % MAX_LEN;
	}
}