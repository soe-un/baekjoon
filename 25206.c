#include <stdio.h>
#include <string.h>

typedef struct {
    char name[51];
    double credit;
    char grade[5];
} SUBJECT;

int main(int argc, char * argv[]) {

    SUBJECT chihoon_subject[20];

    for(int i=0; i<20; i++){
        scanf("%s %lf %s", chihoon_subject[i].name, &chihoon_subject[i].credit, chihoon_subject[i].grade);
    }

    double total_credit = 0;
    double total = 0;
    for(int j=0; j<20; j++){
        if(strncmp(chihoon_subject[j].grade,"P",2)==0) continue;
        total_credit += chihoon_subject[j].credit;
        if(strncmp(chihoon_subject[j].grade,"A+", 2)==0){
            total += chihoon_subject[j].credit * 4.5;
            continue;
        }
        if(strncmp(chihoon_subject[j].grade,"A0", 2)==0){
            total += chihoon_subject[j].credit * 4.0;
            continue;
        }
        if(strncmp(chihoon_subject[j].grade,"B+", 2)==0){
            total += chihoon_subject[j].credit * 3.5;
            continue;
        }
        if(strncmp(chihoon_subject[j].grade,"B0", 2)==0){
            total += chihoon_subject[j].credit * 3.0;
            continue;
        }
        if(strncmp(chihoon_subject[j].grade,"C+", 2)==0){
            total += chihoon_subject[j].credit * 2.5;
            continue;
        }
        if(strncmp(chihoon_subject[j].grade,"C0", 2)==0){
            total += chihoon_subject[j].credit * 2.0;
            continue;
        }
        if(strncmp(chihoon_subject[j].grade,"D+", 2)==0){
            total += chihoon_subject[j].credit * 1.5;
            continue;
        }
        if(strncmp(chihoon_subject[j].grade,"D0", 2)==0){
            total += chihoon_subject[j].credit * 1.0;
            continue;
        }
        if(strncmp(chihoon_subject[j].grade,"F", 2)==0){
            total += chihoon_subject[j].credit * 0.0;
            continue;
        }
    }

    printf("%lf", total/total_credit);

    return 0;
}
