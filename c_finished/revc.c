#include <stdio.h>
#include <string.h>
#include "read_file.c"

int main(void) {
    text t = read_txt("C:\\Users\\Keith\\PycharmProjects\\Rosalind\\prompts\\rosalind_revc.txt");
    printf("%s\n%d\n", t.ptr, t.fsize);

    char revc[t.fsize];

    for (int i = 0; i <t.fsize; i++) {
        switch (t.ptr[i]) {
            case 'A':
                revc[i] = 'T';
                break;
            case 'T':
                revc[i] = 'A';
                break;
            case 'G':
                revc[i] = 'C';
                break;
            case 'C':
                revc[i] = 'G';
                break;

        }
    }

    printf("%s\n%d\n", revc, sizeof(revc));
    free(t.ptr);

    }

