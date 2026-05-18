# python scheduler
# modularization separating codes
import csv
import argparse
import random

from utils.metrices import (
    calculate_averages,
    print_results_table,
    compare_algorithms
)

def generate_random_processes(n):
    processes = []

    for pid in range(1, n + 1):
        process = {
            "pid": pid,
            "arrival_time": random.randint(0, 10),
            "burst_time": random.randint(1, 10),
            "priority": random.randint(1, 5)

        }
        processes.append(process)
    return processes


def load_processes_from_csv(filename):
    processes = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            processes.append({
                "pid": int(row["pid"]),
                "arrival_time": int(row["arrival_time"]),
                "burst_time": int(row["burst_time"])
            })

    return processes


# importing from algorithm folder
from algorithms.schedulers import (
    fcfs,
    sjf,
    priority_scheduling,
    round_robin

)

# importing from utiles folder
from utils.metrices import (
    calculate_averages,
    print_results_table

)

# importing from visualization folder
from visualization.gantt import draw_gantt_chart

# processes in queue to be executed by scheduling
parser = argparse.ArgumentParser()

parser.add_argument(
    "--file",
    type=str,
    help="CSV input file"
)

# generating random processes
parser.add_argument(
    "--random",
    type=int,
    help="Generate random processes"

)

# for adding random algorithm argument
parser.add_argument(
    "--algorithm",
    type=str,
    choices=["fcfs", "sjf", "priority", "rr"],
    default="fcfs",
    help="scheduling algorithm"
)

#for comparison
parser.add_argument(
    "--compare",
    action="store_true",
    help="Compare all algorithms"
)

# quantum argument
parser.add_argument(
    "--quantum",
    type=int,
    default=12,
    help="Time quantum for Round Robin"
)

args = parser.parse_args()

if args.file:

    processes = load_processes_from_csv(args.file)

elif args.random:

    processes = generate_random_processes(args.random)

else:

    processes = [
        {"pid": 1, "arrival_time": 0, "burst_time": 5, "priority": 2},
        {"pid": 2, "arrival_time": 1, "burst_time": 3, "priority": 1},
        {"pid": 3, "arrival_time": 2, "burst_time": 1, "priority": 5},
    ]

# printing section for the program

print(processes)

for process in processes:
    process["remaining_time"] = process["burst_time"]
    process["started"] = False
    process["response_time"] = 0

#comparison function
if args.compare:

    comparison_data = []

    algorithms = {
        "FCFS": fcfs,
        "SJF": sjf,
        "Priority": priority_scheduling
    }

    for name, algorithm in algorithms.items():

        results = algorithm(processes)

        metrics = calculate_averages(results)

        metrics["Algorithm"] = name

        comparison_data.append(metrics)

    rr_results, _ = round_robin(
        processes,
        quantum=args.quantum
    )

    rr_metrics = calculate_averages(rr_results)

    rr_metrics["Algorithm"] = "Round Robin"

    comparison_data.append(rr_metrics)

    compare_algorithms(comparison_data)

    exit()

gantt = []

if args.algorithm == "fcfs":
    results = fcfs(processes)
elif args.algorithm == "sjf":
    results = sjf(processes)
elif args.algorithm == "priority":
    results = priority_scheduling(processes)
elif args.algorithm == "rr":
    results, gantt = round_robin(processes, quantum=args.quantum)

print_results_table(results)

print("\nSUMMARY METRICS")

summary = calculate_averages(results)

for key, value in summary.items():
    print(f"{key}: {value:.2f}")
if gantt:
    draw_gantt_chart(gantt)
