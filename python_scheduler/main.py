# python scheduler
# modularization separating codes

import csv
import argparse
import random
import os

from controller.main_controller import (
    run_scheduler,
    generate_summary,
    export_and_visualize,
    run_c_scheduler
)

from utils.metrics import (
    calculate_averages,
    print_results_table,
    compare_algorithms
)

from visualization.gantt import (
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
    base_dir = os.path.dirname(__file__)

    full_path = os.path.join(
        base_dir,
        filename
    )

    print(full_path)

    processes = []

    with open(full_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row)

            process = {
                "pid": int(row["pid"]),
                "arrival_time": int(row["arrival_time"]),
                "burst_time": int(row["burst_time"]),
                "priority": int(row["priority"]),
                "state": "READY"
            }

            processes.append(process)

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

    parser.add_argument(
        "--c-run",
        action="store_true",
        help="Run C scheduler core"
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
            {"pid": 1, "arrival_time": 0, "burst_time": 5, "priority": 2, "state": "READY"},
            {"pid": 2, "arrival_time": 1, "burst_time": 3, "priority": 1, "state": "READY"},
            {"pid": 3, "arrival_time": 2, "burst_time": 8, "priority": 4, "state": "READY"}
        ]

    if args.c_run:
        run_c_scheduler()

        exit()

    # COMPARISON MODE
    if args.compare:

        if args.c_run:
            run_scheduler()
            exit()

        comparison_data = []

        algorithms = {
            "FCFS": fcfs,
            "SJF": sjf,
            "Priority": priority_scheduling
        }

        for name, algorithm in algorithms.items():
            results, _ = algorithm(processes)

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

        print(comparison_data)

        compare_algorithms(comparison_data)

        draw_comparison_chart(comparison_data)

        # SINGLE ALGORITHM MODE

    # SINGLE ALGORITHM MODE
    else:

        results, gantt = run_scheduler(
            args.algorithm,
            processes,
            args.quantum
        )

        print_results_table(results)

        summary_data = generate_summary(results)

        export_and_visualize(
            results,
            gantt
        )

        print("\n=== SUMMARY METRICS ===")

        for key, value in summary_data[
            "summary"
        ].items():
            print(f"{key}: {value:.2f}")

        print(
            f"\nCPU Utilization: "
            f"{summary_data['cpu_utilization']:.2f}%"
        )

        print(
            f"Throughput: "
            f"{summary_data['throughput']:.2f} "
            f"processes/unit time"
        )
