#include <stdio.h>
#include <string.h>

int main(int argc, char * argv[]) {
    char s[1000001];
    int n[26]={0,};
    gets(s);

    int str_len = strlen(s);

    for(int i = 0 ; i < str_len; i++) {
        if(s[i] >='a' && s[i] <= 'z') s[i] = s[i]-32;
        n[s[i]-'A']++;
    }

    int max = 0;
    int max_idx = 0;
    int max_cnt=0;
    
    for(int j = 0; j < 26; j ++){
        if(n[j] > max) {
            max=n[j];
            max_idx=j;
        }
    }
    
    for(int k=0; k<26; k++) {
        if(n[k] == max) max_cnt++;
    }

    if(max_cnt >= 2) printf("?");
    else printf("%c",'A'+max_idx);

    return 0;
}
