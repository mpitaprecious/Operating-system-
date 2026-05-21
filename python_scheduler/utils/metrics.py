from tabulate import tabulate


# finding the average between processes
def calculate_averages(results):
    n = len(results)
    if n == 0:
        return {
            "avg_waiting_time": 0,
            "avg_turnaround_time": 0,
            "avg_response_time": 0

        }

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


# result table in tabular form
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
            r["response_time"],
            r["state"]
        ])

    headers = [
        "PID",
        "Arrival",
        "Burst",
        "Completion",
        "TAT",
        "WT",
        "RT",
        "state"
    ]

    print(tabulate(table, headers=headers, tablefmt="grid"))


# comparison function
def compare_algorithms(comparison_data):

    from tabulate import tabulate

    table = []

    for row in comparison_data:

        table.append([
            row["Algorithm"],
            f'{row["avg_waiting_time"]:.2f}',
            f'{row["avg_turnaround_time"]:.2f}',
            f'{row["avg_response_time"]:.2f}'
        ])

    headers = [
        "Algorithm",
        "Avg WT",
        "Avg TAT",
        "Avg RT"
    ]

    print(
        tabulate(
            table,
            headers=headers,
            tablefmt="grid"
        )
    )


def calculate_cpu_utilization(results):
    if not results:
        return 0

    total_burst = sum(
        p["burst_time"]
        for p in results
    )

    total_time = max(
        p["completion_time"]
        for p in results
    )

    utilization = (
                          total_burst / total_time
                  ) * 100

    return utilization


def calculate_throughput(results):
    if not results:
        return 0

    completed_processes = len(results)

    total_time = max(
        p["completion_time"]
        for p in results
    )

    throughput = (
            completed_processes / total_time
    )

    return throughput

def calculate_metrics(results):
    """
    Computes average scheduling metrics
    """

    n = len(results)

    if n == 0:
        return {
            "avg_waiting_time": 0,
            "avg_turnaround_time": 0,
            "avg_response_time": 0
        }

    avg_wt = sum(p["waiting_time"] for p in results) / n
    avg_tat = sum(p["turnaround_time"] for p in results) / n
    avg_rt = sum(p["response_time"] for p in results) / n

    return {
        "avg_waiting_time": avg_wt,
        "avg_turnaround_time": avg_tat,
        "avg_response_time": avg_rt
    }