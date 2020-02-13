#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
// dead1
// Hexdump taking a command line argument in the form of a file.

int main(argc,filename)
int argc;
char *filename[];
{
    char red[12] = "\033[0;31m";
    char clear[12] = "\033[0m";
    char feed[20] = "0";
    int i = 0, j = 0;
    int offset = 0;

    if (fopen(filename[1], "r")) {
        FILE *fp = fopen(filename[1], "r");
        printf("%sOffset\tHexadecimal Data Format\t\t\t\t\tCharacter Format%s\n", red, clear);
        while ((feed[i] = fgetc(fp)) != EOF) {
            if (i == 0) {
                printf("%05X\t", offset);
                offset += 16;
            }
            if (i >= 0 && i < 16) {
                printf("%02X ", feed[i]);
            }
            if (feed[i] < 33 || feed[i] > 126) {
                feed[i] = 0x2e;
            }
            i++;
            j = i;
            if (i == 16) {
                printf("\t%s\n", feed);
                i = 0;
            }
        }
        while (j < 16) {
            feed[j] = 0x20;
            printf("   ", feed[j]);
            j++;
        }
        if (i != 0) {
            printf("\t%s\n", feed);
        }
        fclose(fp);
    } else {
        printf("%sFile Does Not Exist.%s\n", red, clear);
    }
    printf("\n");
    return 0;
}
