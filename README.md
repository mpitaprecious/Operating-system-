# Operating-system-
Assignment 1
this is my first commit in github 
its really amazing learning using github although its confusing at first


# EduOS Simulator
A sample operating system simulation built in Python and C that demonstrates process scheduling,
threading and IPC concepts

## name: Precious Mpita
## RegNo:25311351032
## module code: 351 CS 2104


# The simulator combines:

* Python for scheduling control, visualization, and reporting
* C for low-level operating system simulation and threading

## Features

### Python Scheduler

* FCFS Scheduling
* SJF Scheduling
* Priority Scheduling
* Round Robin Scheduling
* CSV Process Loading
* Scheduler Metrics
* Gantt Chart Visualization
* Algorithm Comparison Charts

### C Core Modules

* Process Queue Management
* Thread Creation using pthreads
* Mutex Synchronization
* IPC using Pipes
* Shared Memory Communication
* Deadlock Demonstration
* Race Condition Demonstration


## Technologies used
-Python
-C
-CSV for input data
-Matplotlib for visualization
-pthread 
-GCC / MinGW
-GitHub for version control

## Project structure
EduOS_YourID/
C_core/
Python_scheduler/
controller/
README.md

# Exact structure
EduOS_YourID/

├── README.md
├── .gitignore

├── c_core/
│   ├── main_sim.c
│   ├── process_manager.c
│   ├── thread_manager.c
│   ├── ipc_module.c
│   ├── race_demo.c
│   ├── fixed_demo.c
│   ├── deadlock_demo.c
│   ├── shared_memory_demo.c
│   ├── Makefile
│   └── include/eduos.h

├── python_scheduler/
│   ├── main.py
│   ├── sample_processes.csv
│   ├── requirements.txt
│   ├── algorithms/
│   ├── controller/
│   ├── utils/
│   └── visualization/

├── docs/
│   ├── report.pdf
│   └── screenshots/


## Setup
1.clone the repository
2.install dependencies:
   pip install -r python_scheduler/requirements.txt
3.Run main file:
   python controller/main_controller.py


## Threading and Synchronization

The project demonstrates:

* pthread thread creation
* mutex locking
* race conditions
* deadlock scenarios
* deadlock prevention


## Syllabus Mapping Table

| Syllabus Topic  | Implementation          | File             |
| --------------- | ----------------------- | ---------------- |
| CPU Scheduling  | FCFS, SJF, RR           | schedulers.py    |
| PCB             | Process Control Block   | pcb.py           |
| Threading       | pthreads                | thread_manager.c |
| IPC             | Pipes and shared memory | ipc_module.c     |
| Synchronization | Mutex locks             | fixed_demo.c     |
| Deadlock        | Deadlock scenario       | deadlock_demo.c  |


## Race Condition Demonstration

Two versions were implemented:

- race_demo.c → demonstrates unsafe shared counter access
- fixed_demo.c → demonstrates mutex-protected synchronization

The race version produces inconsistent counter values due to concurrent access,
while the fixed version consistently produces the correct result.

## Running Python Scheduler

cd python_scheduler

python main.py --algorithm fcfs --file sample_processes.csv

## Running Comparison Mode

python main.py --compare --file sample_processes.csv

## Running C Core

python main.py --c-run

## running deadlock_demo.c
gcc deadlock_demo.c -o deadlock_demo -lpthread
.\deadlock_demo.c

## running deadlock_fixed.c
gcc deadlock_fixed.c -o deadlock_fixed -lpthread
.\deadlock_fixed.c 


## IPC and Shared Memory

IPC was implemented using:

* pipes
* shared memory communication

Shared memory concepts were demonstrated using Windows-compatible APIs.

# Screenshots

Screenshots and generated charts are available in:

docs/screenshots/


## Report
[Project Report](docs/report.pdf)


## Challenges Faced

* GCC configuration on Windows
* CSV parsing issues
* Python module imports
* Windows compatibility for shared memory
* Thread synchronization bugs
* indentation  

## Conclusion

The EduOS simulator successfully demonstrates major operating system concepts through a 
hybrid Python and C implementation. The project combines process scheduling, threading,
synchronization, IPC, and visualization into a unified educational operating system simulator.


## References

* Python Documentation
* GCC Documentation
* pthread Documentation
* Operating System Concepts by Silberschatz



