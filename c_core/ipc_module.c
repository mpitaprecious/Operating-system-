#include <stdio.h>
#include <string.h>

#include <io.h>
#include <fcntl.h>

void run_ipc_demo() {

    int fd[2];

    char write_msg[] =
        "Message from Process A";

    char read_msg[100];

    _pipe(
        fd,
        100,
        _O_TEXT
    );

    write(
        fd[1],
        write_msg,
        strlen(write_msg) + 1
    );

    read(
        fd[0],
        read_msg,
        sizeof(read_msg)
    );

    printf(
        "Received message: %s\n",
        read_msg
    );
}