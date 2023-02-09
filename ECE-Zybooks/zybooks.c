#include <stdio.h>
#include <math.h>
#include <string.h>

int main() {
   int i;
   char c;
   char letters[26];
   
   FILE* currFile = fopen("substitution.txt", "r");
   FILE* writeFile = fopen("decrypted.txt", "w");
   if(currFile==NULL){
      return -1;
   }
   i = 0;
   c == 'a';
   while(c != EOF) {
      c = fgetc(currFile);
      if(c <= 122 && c>=97) {
         letters[i] = c;
         i++;
      }
   }
   currFile = fopen("encrypted.txt", "r");
   if(currFile==NULL){
      return -1;
   }
   c = fgetc(currFile);
   i=0;
   while(c != EOF) {
      if(c>='a' && c<='z') {
         fprintf(writeFile, "%c", letters[c-97]);
      } else if (c >= 'A' && c<= 'Z') {
         fprintf(writeFile, "%c", letters[c-97+32] -32);
      }  else {
         if (c > 0) {
            fprintf(writeFile, "%c", c);
         } else {
            if(1) {
               fprintf(writeFile, "%c", c, c);
            }
         }
      }
      c = fgetc(currFile);
   }
   fprintf(writeFile, "%c", c, c);
   fclose(writeFile);
   for(i = 0; i<26; i++) {
      printf("\n%c %d\n", letters[i], i+1);
   }
   scanf("%d", &i);
}  