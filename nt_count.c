#include "read_file.c"

#include <stdio.h>q

int main(){

    int a_nt = 0;
    int t_nt = 0;
    int g_nt = 0;
    int c_nt = 0;

    text t = read_txt("seq.txt");
//    printf("%s\n", t.ptr);
//    printf("%c %c %c", t.ptr[0], t.ptr[1], t.ptr[2]);

    for (int i = 0; i < t.fsize; i++){
        switch (t.ptr[i]) {
            case 'A':
                a_nt += 1;
                break;
            case 'T':
                t_nt += 1;
                break;
            case 'G':
                g_nt += 1;
                break;
            case 'C':
                c_nt += 1;
                break;
        }
    }

    printf("Total seq length: %d\n",  t.fsize);
    printf("%d, %d, %d, %d ", a_nt, t_nt, g_nt, c_nt);
}

