# python scheduler
# modularization separating codes
import csv
import argparse
import random



def generate_random_processes(n):

    processes = []

    for pid in range(1, n + 1):
        process = {
            "pid": pid,
            "arrival_time": random.randint(0, 10),
            "burst_time": random.randint(1,10),
            "priority": random.randint(1,5)

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
parser.add_argument(
    "--random",
    type=int,
    help="Generate random processes"

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

results, gantt = round_robin(processes, quantum=2)

print_results_table(results)

print("\nSUMMARY METRICS")

summary = calculate_averages(results)

for key, value in summary.items():
    print(f"{key}: {value:.2f}")

draw_gantt_chart(gantt)
