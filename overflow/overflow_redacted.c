#include <stdio.h>
#include <string.h>

char flag[] = "not_the_real_flag";

int main(int argc, char *argv[]) {
  int data = 0xdeadbeef;
  char buf[1024];

  printf("What's your name? ");
  fflush(stdout);

  gets(buf);

  printf("Hi %s\n", buf);
  fflush(stdout);

  if (data != 0xdeadbeef) {
    printf("How did this happen? Here is your flag: \"%s\"\n", flag);
  }

  return 0;
}

