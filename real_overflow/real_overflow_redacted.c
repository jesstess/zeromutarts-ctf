#include <stdio.h>
#include <string.h>

char flag[] = "not_the_real_flag";

void printf_flag(void) {
  printf("Well done! here is your flag: %s\n", flag);
  fflush(stdout);
}

int main(int argc, char *argv[]) {
  char buf[1024];

  printf("Oh you again, did you know that the address of print_flag is at %p?\nCan you tell me your name again? ", printf_flag);
  fflush(stdout);

  gets(buf);

  printf("Hi %s\n", buf);
  fflush(stdout);

  return 0;
}

