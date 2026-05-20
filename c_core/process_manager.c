#include <stdio.h>
#include "include/eduos.h"

void create_process(
    PCB *process,
    int pid,
    int arrival,
    int burst,
    int priority
) {

    process->pid = pid;
    process->arrival_time = arrival;
    process->burst_time = burst;
    process->priority = priority;

    process->completion_time = 0;
    process->turnaround_time = 0;
    process->waiting_time = 0;
    process->response_time = 0;

    process->state = READY;
}

void display_process(PCB process) {

    printf(
        "PID: %d | Arrival: %d | Burst: %d | Priority: %d\n",
        process.pid,
        process.arrival_time,
        process.burst_time,
        process.priority
    );
}