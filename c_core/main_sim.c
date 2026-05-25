#include <stdio.h>

#include "include/eduos.h"

int main() {

    printf(
        "\n=== IPC DEMO ===\n\n"
    );

    run_ipc_demo();
    save_pcb_snapshot();
    printf("Eduos simulator starting...\n");
    edu_wait(1, 2);

    return 0;
}

