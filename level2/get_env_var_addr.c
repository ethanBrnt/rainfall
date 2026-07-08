#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    char *ptr = getenv("payload");
    printf("addr: %p\n", ptr);
}