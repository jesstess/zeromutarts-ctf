#include <stdio.h>

char flag[] = "not_the_real_flag";

char password[] = "not_the_real_password";

int main(int argc, char *argv[]) {
  int i;
  char buf[sizeof(password)+1];

  printf("Password: ");

  fgets(buf, sizeof(buf)-1, stdin);
  buf[sizeof(buf)] = 0;

  if (strcmp(password, buf) != 0) {
    puts("That was the wrong password.");
    return 1;
  }

  for (i = 0; i < sizeof(flag)-1; ++i) {
    flag[i] = flag[i] ^ 0x80;
  }

  printf("\nCongratulations! Your flag is: \"%s\"\n", flag);

  return 0;
}

