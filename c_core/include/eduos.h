#ifndef EDUOS_H
#define EDUOS_H

#define MAX_PROCESSES 100

typedef enum {
    READY,
    RUNNING,
    WAITING,
    TERMINATED
} ProcessState;

typedef struct {

    int pid;
    int arrival_time;
    int burst_time;
    int priority;

    int completion_time;
    int turnaround_time;
    int waiting_time;
    int response_time;

    ProcessState state;

} PCB;

void create_process(
    PCB *process,
    int pid,
    int arrival,
    int burst,
    int priority
);

void display_process(
    PCB process
);

#endif