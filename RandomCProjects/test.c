#include <stdio.h>
int function() {
    return ('a' == 'a');
}
int main() {
    if(function()) {
        printf("lemon\n");
    }
    return 0;
}