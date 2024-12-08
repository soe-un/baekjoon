#include <stdio.h>

int main(int argc, char * argv[]) {
    int a;
    char str[1000];
    
    scanf("%s", str);
    scanf("%d", &a);


    printf("%c", str[a-1]);

    return 0;
}
