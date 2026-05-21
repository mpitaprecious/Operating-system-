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

typedef struct {

    PCB items[MAX_PROCESSES];

    int front;
    int rear;

} Queue;

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

void fcfs(
    PCB processes[],
    int n
);

void init_queue(
    Queue *q
);

int is_empty(
    Queue *q
);

void enqueue(
    Queue *q,
    PCB process
);

PCB dequeue(
    Queue *q
);

void* thread_function(
    void *arg
);

void run_ipc_demo();

#endif