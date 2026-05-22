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


## Features
-FCFS scheduling 
-SJF scheduling
-Priority Scheduler
-Round Robin Scheduling
-Process control block
-Queue Management
-Threading management simulation
-Mutex Synchronization
-Python + c Hybrid Architecture
-IPC modules
-Gantt chart visualization

## Technologies used
-Python
-C
-CSV for input data
-Matplotlib for visualization
-pthread 
-GCC / MinGW

## Project structure
C_core/
Python_scheduler/
controller/
README.md

## Setup
1.clone the repository
2.install dependencies:
   pip install -r python_scheduler/requirements.txt
3.Run main file:
   python controller/main_controller.py


## output
example for gantt and bar chart
![Figure 1 5_17_2026 9_41_40 PM.png](docs/screenshots/Figure%201%205_17_2026%209_41_40%20PM.png)
![scheduling algorithm comparison.png](docs/screenshots/scheduling%20algorithm%20comparison.png)

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


## Bonus Features

- IPC module
- Mutex synchronization
- Python/C hybrid architecture

## Report
[Project Report](docs/report.pdf)