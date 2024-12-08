#include <stdio.h>
#include <string.h>

int main(int argc, char * argv[]) {
    char s[101];    
    scanf("%s", s);

    int aph_cnt = strlen(s);

    char for_croatic_aph[8][4] = {
        "c=",
        "c-",
        "dz=",
        "d-",
        "lj",
        "nj",
        "s=",
        "z=",
    };

    for(int i=0;i<8;i++){
        char *croatic_aph= strstr(s, for_croatic_aph[i]);
        while(croatic_aph != NULL) {
            if(i==2) aph_cnt=aph_cnt-2;
            else aph_cnt--;
            if(i==2) strncpy(croatic_aph, "@@@", 3);
            else strncpy(croatic_aph, "@@", 2);
            croatic_aph=strstr(croatic_aph+1, for_croatic_aph[i]);
        }
    }

    printf("%d", aph_cnt);
    return 0;
}
