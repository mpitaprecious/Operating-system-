import subprocess
import os



from algorithms.schedulers import (
    fcfs,
    sjf,
    priority_scheduling,
    round_robin
)

from utils.metrics import (
    calculate_averages,
    calculate_cpu_utilization,
    calculate_throughput
)

from visualization.gantt import (
    draw_gantt_chart,
    draw_comparison_chart
)

from utils.report import export_results


def run_scheduler(
    algorithm,
    processes,
    quantum=2
):

    gantt = []

    if algorithm == "fcfs":

        results, gantt = fcfs(processes)

    elif algorithm == "sjf":

        results, gantt = sjf(processes)

    elif algorithm == "priority":

        results, gantt = priority_scheduling(processes)

    elif algorithm == "rr":

        results, gantt = round_robin(
            processes,
            quantum
        )

    else:

        raise ValueError(
            "Invalid scheduling algorithm"
        )

    return results, gantt


def generate_summary(results):

    summary = calculate_averages(results)

    cpu = calculate_cpu_utilization(results)

    throughput = calculate_throughput(results)

    return {
        "summary": summary,
        "cpu_utilization": cpu,
        "throughput": throughput
    }


def export_and_visualize(results, gantt):

    export_results(results)

    if gantt:
        draw_gantt_chart(gantt)

def run_c_scheduler():

    c_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "c_core",
        "eduos.exe"
    )

    c_path = os.path.abspath(c_path)

    print("\nLaunching C Scheduler...\n")

    result = subprocess.run(
        [c_path],
        capture_output=True,
        text=True
    )

    print(result.stdout)