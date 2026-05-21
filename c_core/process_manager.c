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


void fcfs(
    PCB processes[],
    int n
) {

    int time = 0;

    for (int i = 0; i < n; i++) {

        if (time < processes[i].arrival_time) {

            time = processes[i].arrival_time;
        }

        processes[i].state = RUNNING;

        int start = time;

        int completion =
            start +
            processes[i].burst_time;

        processes[i].completion_time =
            completion;

        processes[i].turnaround_time =
            completion -
            processes[i].arrival_time;

        processes[i].waiting_time =
            processes[i].turnaround_time -
            processes[i].burst_time;

        processes[i].response_time =
            start -
            processes[i].arrival_time;

        processes[i].state = TERMINATED;

        time = completion;
    }
}

void init_queue(Queue *q) {

    q->front = 0;

    q->rear = -1;
}

int is_empty(Queue *q) {

    return q->rear < q->front;
}

void enqueue(
    Queue *q,
    PCB process
) {

    q->rear++;

    q->items[q->rear] = process;
}

PCB dequeue(Queue *q) {

    PCB process =
        q->items[q->front];

    q->front++;

    return process;
}