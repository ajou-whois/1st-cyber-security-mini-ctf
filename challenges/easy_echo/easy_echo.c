#include <stdio.h>



int main()
{
	char cmd[256];
	char name[256];
	setvbuf(stdout, NULL, _IONBF, 0);
  	setvbuf(stdin, NULL, _IONBF, 0);
	while(1)
	{
		fgets(name, sizeof(name)-1, stdin);
		name[strlen(name)-1] = 0;
		memset(cmd, 0, sizeof(cmd));
		strncat(cmd, "echo hello Jr.", sizeof(cmd)-1);
		strncat(cmd, name, sizeof(cmd)-1);
		strncat(cmd, "!", sizeof(cmd)-1);
		cmd[strlen(cmd)-1] = 0;
		printf("command : %s\n", cmd);
		system(cmd);
	}
	return 0;
}
