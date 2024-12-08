#include <stdio.h>

int main(int argc, char * argv[]) {
    int answer[6] = {1, 1, 2, 2, 2, 8};
    int input[6] = {0,};
    int res[6] = {0,};

    for(int i = 0 ; i < 6 ; i ++){
        scanf("%d", &input[i]);
    }

    for(int i = 0 ; i < 6 ; i ++) {
        res[i] = answer[i] - input[i];
    }

    for(int i = 0 ; i < 6 ; i ++){
        printf("%d ", res[i]);
    }

    return 0;
}