#include <stdio.h>
#include <string.h>
#include <fcntl.h>

int main()
{
    char input[256] = {0};
    char path[256] = {0};
    char buf[256] = {0};
    int fd, flag_fd;
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    fgets(input, sizeof(input) - 1, stdin);
    char *end = strchr(input, '\n');
    if(end)
         *end = 0;
    flag_fd = open("/home/easy_readfile/flag", O_RDONLY);
    if(flag_fd == -1)
    {
        perror("failed to read flag");
        return 1;
    }
    if(strstr(input, "flag"))
    {
        perror("that's no no. you cannot read flag");
        return 1;
    }
    fd = open(input, O_RDONLY);
    if(fd == -1)
    {
        perror("Error");
        return 1;
    }
    read(fd, buf, sizeof(buf) - 1);
    fprintf(stdout, "%s", buf);
    close(fd);
    close(flag_fd);

}
