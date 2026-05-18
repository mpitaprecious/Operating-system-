from tabulate import tabulate

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
            r["response_time"]
        ])

    headers = [
        "PID",
        "Arrival",
        "Burst",
        "Completion",
        "TAT",
        "WT",
        "RT"
    ]

    print(tabulate(table, headers=headers, tablefmt="grid"))

#comparison function
def compare_algorithms(comparison_data):

    from tabulate import tabulate

    table = []

    for row in comparison_data:

        table.append([
            row["Algorithm"],
            f'{row["Average Waiting Time"]:.2f}',
            f'{row["Average Turnaround Time"]:.2f}',
            f'{row["Average Response Time"]:.2f}',
            f'{row["CPU Utilisation"]:.2f}',
            f'{row["Throughput"]:.2f}'
        ])

    headers = [
        "Algorithm",
        "Avg WT",
        "Avg TAT",
        "Avg RT",
        "CPU %",
        "Throughput"
    ]

    print(tabulate(table, headers=headers, tablefmt="grid"))