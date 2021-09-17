#include <errno.h>
#include <stdio.h>

typedef struct {
    char* ptr;
    unsigned long fsize;
} text ;

text read_txt(char fname[]){
     // pointer to buffer which will store file contents and filesize
    char* buff;
    unsigned long fsize;
    text t;
    int errnum;

    FILE* fp = fopen(fname, "rb");
    if (fp == NULL) {
        // assign error number
        errnum = errno;
        // fprintf allows other output streams beside stdout
        fprintf(stderr, "Error opening file: %s\n", strerror(errnum));
        exit(1);
    }

    // fseek sets position to start file position at end of file. 0 is offset bytes from end of file
    fseek(fp, 0, SEEK_END);
    // ftell returns current file position of file stream. i.e. the total size of file in bytes. add 1
    fsize = ftell(fp);
    // rewind fstream to start to begin reading contents
    rewind(fp);

    // set buff memory location equal to fsize * size of char type (8 bits or 1 byte)
    buff = (char*)malloc(fsize);
    // read file contents to buffer
    int ret_code = fread(buff, 1, fsize, fp);
    // close file
    fclose(fp);

    // if number of characters read is equal to file size
    if (ret_code == fsize){
        t.fsize = fsize;
        t.ptr = buff;
        // printf("%s", buff);
        // return pointer to buffer but don't forget to free memory after use!
        return t;
        // free(buff);
    }
    else {
        fprintf(stderr, "Error reading file.\n");
        free(buff);
        exit(1);
    }

}

//int main() {
//    int msg;
//    msg = read_txt("seq.txt");
//    printf("%s\n", msg);
//    free(msg);}
