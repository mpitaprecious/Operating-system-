#python scheduler
pip install tabulate
from tabulate import tabulate


# first come first serve scheduling
def fcfs(processes):
    processes = sorted(
        processes,
        key=lambda x: (x["arrival_time"], x["pid"])
    )

    time = 0
    results = []

    for process in processes:

        if time < process["arrival_time"]:
            time = process["arrival_time"]

        start = time
        completion = start + process["burst_time"]

        tat = completion - process["arrival_time"]
        wt = tat - process["burst_time"]
        rt = start - process["arrival_time"]

        results.append({
            "pid": process["pid"],
            "arrival_time": process["arrival_time"],
            "burst_time": process["burst_time"],
            "start_time": start,
            "completion_time": completion,
            "turnaround_time": tat,
            "waiting_time": wt,
            "response_time": rt
        })

        time = completion

    return results


# shortest job first scheduling
def sjf(processes):
    processes = sorted(
        processes,
        key=lambda x: (x["arrival_time"], x["pid"])
    )

    completed = []
    ready_queue = []

    time = 0
    index = 0
    n = len(processes)

    while len(completed) < n:

        while index < n and processes[index]["arrival_time"] <= time:
            ready_queue.append(processes[index])
            index += 1

        if not ready_queue:
            time += 1
            continue

        ready_queue.sort(
            key=lambda x: (
                x["burst_time"],
                x["arrival_time"],
                x["pid"]
            )
        )

        process = ready_queue.pop(0)

        start = time
        completion = start + process["burst_time"]

        tat = completion - process["arrival_time"]
        wt = tat - process["burst_time"]
        rt = start - process["arrival_time"]

        completed.append({
            "pid": process["pid"],
            "arrival_time": process["arrival_time"],
            "burst_time": process["burst_time"],
            "start_time": start,
            "completion_time": completion,
            "turnaround_time": tat,
            "waiting_time": wt,
            "response_time": rt
        })

        time = completion

    return completed


# finding the average between processes
def calculate_averages(results):
    n = len(results)

    avg_wt = sum(r["waiting_time"] for r in results) / n
    avg_tat = sum(r["turnaround_time"] for r in results) / n
    avg_rt = sum(r["response_time"] for r in results) / n

    total_burst = sum(r["burst_time"] for r in results)

    total_time = max(r["completion_time"] for r in results)

    cpu_util = (total_burst / total_time) * 100

    throughput = n / total_time

    return {
        "Average Waiting Time": avg_wt,
        "Average Turnaround Time": avg_tat,
        "Average Response Time": avg_rt,
        "CPU Utilisation": cpu_util,
        "Throughput": throughput
    }


def print_results_table(results):
    table = []
    for r in results:
        table.append([
            r["pid"],
            r["arrival_time"],
            r["burst_time"],
            r["completion_time"],
            r["turnaround_time"],
            r["waiting_time"],
            r["response_time"]

        ])

    headers = [
        "PID",
        "Arrival",
        "Burst"
        "Completion",
        "TAT",
        "WT",
        "RT"
    ]


print(tabulate(table, headers=headers, tablefmt="grid"))


processes = [
    {"pid": 1, "arrival_time": 0, "burst_time": 5},
    {"pid": 2, "arrival_time": 1, "burst_time": 3},
    {"pid": 3, "arrival_time": 2, "burst_time": 1},
]


# priority scheduling
def priority_scheduling(processes):
    processes = sorted(
        processes,
        key=lambda x: (x["arrival_time"], x["pid"])
    )

    completed = []
    ready_queue = []

    time = 0
    index = 0
    n = len(processes)

    while len(completed) < n:

        while index < n and processes[index]["arrival_time"] <= time:
            process = processes[index].copy()

            process["current_priority"] = process["priority"]

            ready_queue.append(process)

            index += 1

        if not ready_queue:
            time += 1
            continue

        for process in ready_queue:
            waiting_time = time - process["arrival_time"]

            ageing_steps = waiting_time // 3

            improved_priority = process["priority"] - ageing_steps

            process["current_priority"] = max(0, improved_priority)

        ready_queue.sort(
            key=lambda x: (
                x["current_priority"],
                x["arrival_time"],
                x["pid"]
            )
        )

        process = ready_queue.pop(0)

        start = time
        completion = start + process["burst_time"]

        tat = completion - process["arrival_time"]
        wt = tat - process["burst_time"]
        rt = start - process["arrival_time"]

        completed.append({
            "pid": process["pid"],
            "priority": process["current_priority"],
            "arrival_time": process["arrival_time"],
            "burst_time": process["burst_time"],
            "start_time": start,
            "completion_time": completion,
            "turnaround_time": tat,
            "waiting_time": wt,
            "response_time": rt
        })

        time = completion

    return completed


# round robin scheduling
def round_robin(processes, quantum=2):
    processes = sorted(
        processes,
        key=lambda x: (x["arrival_time"], x["pid"])
    )

    ready_queue = []
    completed = []

    time = 0
    index = 0
    n = len(processes)

    for process in processes:
        process["remaining_time"] = process["burst_time"]
        process["started"] = False

    while len(completed) < n:

        while index < n and processes[index]["arrival_time"] <= time:
            ready_queue.append(processes[index])
            index += 1

        if not ready_queue:
            time += 1
            continue

        process = ready_queue.pop(0)

        if not process["started"]:
            process["response_time"] = time - process["arrival_time"]
            process["started"] = True

        execution_time = min(quantum, process["remaining_time"])

        start = time
        time += execution_time

        process["remaining_time"] -= execution_time

        while index < n and processes[index]["arrival_time"] <= time:
            ready_queue.append(processes[index])
            index += 1

        if process["remaining_time"] > 0:

            ready_queue.append(process)

        else:

            completion = time

            tat = completion - process["arrival_time"]

            wt = tat - process["burst_time"]

            completed.append({
                "pid": process["pid"],
                "arrival_time": process["arrival_time"],
                "burst_time": process["burst_time"],
                "completion_time": completion,
                "turnaround_time": tat,
                "waiting_time": wt,
                "response_time": process["response_time"]
            })

    return completed


# printing section for the program

results = round_robin(processes, quantum=2)
print_result_table(results)

print("\nSUMMARY METRICS")

summary = calculate_averages(results)

for key, value in summary.items():
    print(f"{key}: {value:.2f}")
