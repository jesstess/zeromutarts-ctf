#include <stdio.h>

int main(int argc, char *argv[]) {
  char buf[0x1000];
  fgets(buf, sizeof(buf), stdin);
  ((void (*)(void)) buf)();
}

