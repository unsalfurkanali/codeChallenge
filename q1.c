#include <stdio.h>
int prime(int x);
int sophie(int x);
int harshad(int x);
int main(void) {
    int i;
    int password = 0;

    for(i = 999; i > 100; i--) {
        if(sophie(i)) {
            password = password + i;
            break;
        }
        else ;
    }
    for(i = 1000; i < 10000; i++) {
        if(harshad(i)) {
            password = password + i;
            break;
        }
        else ;
    }
    printf("Password = %d", password);
    return 0;
}

int prime(int x) {
    int i;
    for(i = 2; i < x; i++) {
        if(!(x%i)) return 0;
        else ;
    }
    return 1;
}

int sophie(int x) {
    if(prime(x) && prime(2*x+1)) return 1;
    else return 0;
}

int harshad(int x) {
    int sum = 0;
    while(1) {
        sum = x % 10 + sum;
        x = x / 10;
        if(x<10) break;
    }
    sum = sum + x;
    if(!(x%sum)) return 1;
    else return 0;
}