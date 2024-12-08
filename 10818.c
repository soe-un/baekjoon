#include <stdio.h>

int main(int argc, char * argv[]) {
    int a;
    scanf("%d", &a);
    int num[a];
    
    for (int i=0;i < a;i++) {
        scanf("%d", &num[i]);
    }


    int minV = 1000001;
    int maxV = -1000001;


    for (int j=0; j<a; j++) {
        if(num[j] > maxV) maxV = num[j];
        if(num[j] < minV) minV = num[j];
    }

    printf("%d %d", minV, maxV);
    
    return 0;
}
