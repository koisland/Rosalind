#include "read_file.c"
#include <stdio.h>

int main() {
    text t = read_txt("rosalind_rna.txt");

    // allocate array of same filesize as read text file
    char rna[t.fsize];
    printf("%i\n", sizeof(rna));

    for (int i=0; i < t.fsize; i++) {
        switch (t.ptr[i]) {
            case 'T':
                rna[i] = 'U';
                break;
            default:
                rna[i] = t.ptr[i];
                break;
        }
    }

    printf("%s\n", rna);
    free(t.ptr);

}
