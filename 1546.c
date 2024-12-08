#include <stdio.h>
#include <math.h>

int main(int argc, char * argv[]) {
    int a;
    scanf("%d", &a);
    int num[a];
    
    for (int i=0;i < a;i++) {
        scanf("%d", &num[i]);
    }

    // find Max
    int max = 0;
    for (int j=0; j<a; j++) {
        if(num[j] > max) max = num[j];
    }

    // set Value
    double res[a];
    for (int k=0; k<a; k++) {
        double tmp = (double)num[k] / max * 100;
        res[k]=  (double)floor((tmp * 100)+0.5) / 100;
    }


    // find avearge
    double total = 0;
    for (int l=0; l<a; l++) {
        total += res[l];
    }
    
    printf("%.3lf", total / a);

    return 0;
}
