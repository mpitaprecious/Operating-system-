#include <stdio.h>
#include "include/eduos.h"

int main() {

    PCB p1;

    create_process(
        &p1,
        1,
        0,
        5,
        2
    );

    display_process(p1);

    return 0;
}