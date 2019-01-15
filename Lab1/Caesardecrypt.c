#include <stdio.h>

int main(void)
{
   char messageClear[BUFSIZ];
   char messageCrypt[BUFSIZ];
   int shift, i;

   printf("\nThis program decrypts a capital string using all 25 key values of the Caesar Cipher. \n\n");
   printf("Enter Caesar encrypted string in all capital letters: ");
   fgets(messageCrypt, BUFSIZ, stdin);
   fflush(stdin);

   printf("\nEncrypted Message:%s ", messageCrypt);

   for (shift=0; shift<26; shift++)
   {
      i=0;
      while (messageCrypt[i])
      {
        messageClear[i] = messageCrypt[i] - shift;
	if (messageClear[i] < 'A')
	   messageClear[i] = messageClear[i] + 26;
         i++;
      }
      messageClear[i-1] = '\0';

      printf("Message after %d shifts: %s\n", shift, messageClear);
   }   

}
