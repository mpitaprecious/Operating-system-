#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

#include "include/eduos.h"

pthread_mutex_t lock;

void* thread_function(void *arg) {

    PCB *process = (PCB*) arg;

    pthread_mutex_lock(&lock);

    process->state = RUNNING;

    printf(
        "Thread executing Process %d\n",
        process->pid
    );

    sleep(1);

    process->state = TERMINATED;

    printf(
        "Process %d completed\n",
        process->pid
    );

    pthread_mutex_unlock(&lock);

    pthread_exit(NULL);
}