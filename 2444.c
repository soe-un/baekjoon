#include <stdio.h>

int main(int argc, char * argv[]) {
    int num;
    scanf("%d", &num);
    
    for(int i = 1 ; i < num ; i++){
        for(int j = num-i ; j > 0 ; j--){
            printf(" ");
        }
        for(int k = 1; k <= 2*i-1; k++) {
            printf("*");
        }
        printf("\n");
    }
    
    for(int l = 0 ; l < 2*num-1 ; l++){
        printf("*");
    }
    printf("\n");

    for(int a = 1 ; a < num ; a++){
        for(int b = 0; b < a ; b++){
            printf(" ");
        }
        for(int c = 2*(num-a)-1; c > 0; c--) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}