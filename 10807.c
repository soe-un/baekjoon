#include <stdio.h>

int main(void) {
    int a, b;
    int num[a];
    int res=0;
    
    scanf("%d", &a);
    for (int i=0;i < a;i++) {
        scanf("%d ", &num[i]);
    }
    scanf("%d", &b);

    for(int j=0; j<a; j++) {
        if(num[j] == b) res++;
    }

    printf("%d", res);
    
    return 0;
}
