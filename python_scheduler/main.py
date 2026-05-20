# python scheduler
# modularization separating codes

import csv
import argparse
import random

from utils.pcb import ProcessControlBlock
from utils.report import export_results

from utils.metrices import (
    calculate_averages,
    print_results_table,
    compare_algorithms,
    calculate_cpu_utilization,
    calculate_throughput
)

from visualization.gantt import (
    draw_gantt_chart,
    draw_comparison_chart
)

from algorithms.schedulers import (
    fcfs,
    sjf,
    priority_scheduling,
    round_robin
)

# Clear old logs
open("scheduler.log", "w").close()


# RANDOM PROCESS GENERATOR
def generate_random_processes(n):

    processes = []

    for pid in range(1, n + 1):

        process = {
            "pid": pid,
            "arrival_time": random.randint(0, 10),
            "burst_time": random.randint(1, 10),
            "priority": random.randint(1, 5),
            "state": "READY"
        }

        processes.append(process)

    return processes


# LOAD CSV FILE
def load_processes_from_csv(filename):

    processes = []

    with open(filename, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            process = ProcessControlBlock(
                pid=row["pid"],
                arrival_time=int(row["arrival_time"]),
                burst_time=int(row["burst_time"]),
                priority=int(row["priority"])
            )

            processes.append(process.to_dict())

    return processes

# MAIN EXECUTION
if __name__ == "__main__":

    print("MAIN BLOCK STARTED")

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--algorithm",
        type=str,
        choices=["fcfs", "sjf", "priority", "rr"],
        default="fcfs",
        help="Scheduling algorithm"
    )

    parser.add_argument(
        "--quantum",
        type=int,
        default=2,
        help="Time quantum for Round Robin"
    )

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

    parser.add_argument(
        "--compare",
        action="store_true",
        help="Compare all scheduling algorithms"
    )

    args = parser.parse_args()

    # LOAD PROCESSES
    if args.file:

        processes = load_processes_from_csv(args.file)
        print(processes)

    elif args.random:

        processes = generate_random_processes(args.random)

    else:

        processes = [
            {"pid": 1,"arrival_time": 0,"burst_time": 5,"priority": 2,"state": "READY"},
            {"pid": 2,"arrival_time": 1,"burst_time": 3,"priority": 1,"state": "READY"},
            {"pid": 3,"arrival_time": 2,"burst_time": 8,"priority": 4,"state": "READY"}
        ]

    # COMPARISON MODE
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
            args.quantum
        )

        rr_metrics = calculate_averages(rr_results)

        rr_metrics["Algorithm"] = "Round Robin"

        comparison_data.append(rr_metrics)

        compare_algorithms(comparison_data)

        draw_comparison_chart(comparison_data)

    # SINGLE ALGORITHM MODE
    else:

        gantt = []

        if args.algorithm == "fcfs":

            results,gantt = fcfs(processes)

        elif args.algorithm == "sjf":

            results,gantt = sjf(processes)

        elif args.algorithm == "priority":

            results,gantt = priority_scheduling(processes)

        elif args.algorithm == "rr":

            results, gantt = round_robin(
                processes,
                args.quantum
            )

        else:

            print("Invalid algorithm")
            exit()

        # PRINT RESULTS
        print_results_table(results)

        # EXPORT REPORT
        export_results(results)

        # SUMMARY METRICS
        summary = calculate_averages(results)

        print("\n=== SUMMARY METRICS ===")

        for key, value in summary.items():

            print(f"{key}: {value:.2f}")

        # CPU UTILIZATION
        cpu_util = calculate_cpu_utilization(results)

        print(f"\nCPU Utilization: {cpu_util:.2f}%")

        # THROUGHPUT
        throughput = calculate_throughput(results)

        print(
            f"Throughput: "
            f"{throughput:.2f} processes/unit time"
        )

        # GANTT CHART
        if gantt:

            draw_gantt_chart(gantt)