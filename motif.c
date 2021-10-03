#include <stdio.h>
#include "read_file.c"
#include <string.h>


int KMP_lps(char* ptn, int ptn_len, int* lps){
    // longest length of lps
    int len = 0;

    // starting lps len
    lps[0] = 0;

    // position of next index in ptn
    // only i++ if ptn[i]==ptn[len] or ptn[i]!=ptn[len] && i=0 (lps broken by nonmatch)
    int i = 1;


    while(i < ptn_len) {
        if (ptn[len] == ptn[i]){
            // if match, increment len of lps and i in ptn
            len++;
            lps[i] = len;
            i++;
        }
        else{
            if (len!=0) {
                // change len by decrementing to last previous len since reached mismatch
                len = lps[len-1];
                // don't increment i here because would would inflate lps length. len must return to 0 first.
            }
            else {
                // reset lps index val to 0 at i-th position
                lps[i] = 0;
                // move to i+1-th pos
                i++;
            }
        }
    }
}

int KMP(char* ptn, char* seq){
    // Implementation of main Knuth-Morris-Pratt algorithm
    int seq_len = strlen(seq);
    int ptn_len = strlen(ptn);
    printf("Seq: %d\nPtn: %d\n", seq_len, ptn_len);

    // longest prefix suffix
    int lps[ptn_len];

    // can't return arrays in C
    KMP_lps(ptn, ptn_len, lps);
    printf("LPS: ");
    for (int i=0; i < ptn_len; i++) {
        printf("%d ", lps[i]);
    }
    printf("\n");

    int ptn_i = 0;
    int seq_i = 0;

    while (seq_i < seq_len) {
        // if chr at ptn_i of ptn matches chr at seq_i of seq
        if (ptn[ptn_i] == seq[seq_i]) {
            // increment index of ptn and seq
            ptn_i++;
            seq_i++;
        }
        // if go through entire pattern, pattern has been found
        if (ptn_i > 9) {
            printf("ptn_i: %d\n", ptn_i);
        }

        if (ptn_i == ptn_len) {
            printf("%d\n", seq_i - ptn_i);
            // reset ptn_i to give index of next chr to match.
            ptn_i = lps[ptn_i - 1];

        }
        // mismatch
        else if (seq_i < seq_len && ptn[ptn_i] != seq[seq_i]) {
            if (ptn_i != 0) {
                // skip redoing work after mismatch  lps[0 -> lps[ptn_i-1]] char
                ptn_i = lps[ptn_i - 1];
            }
            else {
                // after mismatch, if ptn_1 == 0, then move on to next chr in seq
                seq_i++;
            }

        }
    }
}
//https://stackoverflow.com/a/63990303/16065715
void slice(const char *str, char *result, size_t start, size_t end) {
    if (end > start) {
        strncpy(result, str + start, end - start);
    }
    else {
        fprintf(stderr, "Error with end and start.");
    }

}

int main() {
    text t = read_txt("rosalind_motif.txt");
    char full_text[t.fsize + 1];

    printf("Total Length: %d\n", t.fsize);

    for (int i=0; i < t.fsize; i++) {
        full_text[i] = t.ptr[i];
    }

    char * match = strchr(full_text, '\n');
    if (match) {
        // subtracting match ptr with string ptr gives how many char they are apart
        size_t index = (match - full_text);
        size_t seq_len = index;
        size_t ptn_len = t.fsize - index;
        char seq[index];
        char ptn[ptn_len];

        slice(full_text, seq, 0, index);
        // start at index  + 1 to avoid \n
        slice(full_text, ptn, index + 1, t.fsize);

        printf("Sequence:\n%s \n\nPattern:\n%s\n", seq, ptn);
        KMP(ptn, seq);
    }

    free(t.ptr);
}
