from collections import deque

from utils.pcb import update_process_state
from utils.logger import log_event


# first come, first served scheduling
def fcfs(processes):

    processes = sorted(
        processes,
        key=lambda x: (x["arrival_time"], x["pid"])
    )

    time = 0
    results = []

    for process in processes:

        # CPU idle handling
        if time < process["arrival_time"]:
            time = process["arrival_time"]

        # Process enters RUNNING state
        update_process_state(process, "RUNNING")

        log_event(
            f"[TIME {time}] Process {process['pid']} entered RUNNING state"
        )

        start = time

        completion = start + process["burst_time"]

        tat = completion - process["arrival_time"]

        wt = tat - process["burst_time"]

        rt = start - process["arrival_time"]

        # Process terminates
        update_process_state(process, "TERMINATED")

        log_event(
            f"[TIME {completion}] Process {process['pid']} TERMINATED"
        )

        results.append({
            "pid": process["pid"],
            "arrival_time": process["arrival_time"],
            "burst_time": process["burst_time"],
            "completion_time": completion,
            "turnaround_time": tat,
            "waiting_time": wt,
            "response_time": rt,
            "state": process["state"]
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

    queue = deque()

    time = 0
    index = 0

    gantt = []
    results = []

    remaining = {}

    for p in processes:
        remaining[p["pid"]] = p["burst_time"]

    while queue or index < len(processes):

        # Add arrived processes
        while (
            index < len(processes)
            and processes[index]["arrival_time"] <= time
        ):

            process = processes[index]

            update_process_state(process, "READY")

            log_event(
                f"[TIME {time}] Process {process['pid']} entered READY state"
            )

            queue.append(process)

            index += 1

        # CPU idle
        if not queue:
            time += 1
            continue

        process = queue.popleft()

        update_process_state(process, "RUNNING")

        log_event(
            f"[TIME {time}] Process {process['pid']} entered RUNNING state"
        )

        start = time

        execute = min(
            quantum,
            remaining[process["pid"]]
        )

        time += execute

        remaining[process["pid"]] -= execute

        gantt.append(
            (
                process["pid"],
                start,
                time
            )
        )

        # Add newly arrived processes during execution
        while (
            index < len(processes)
            and processes[index]["arrival_time"] <= time
        ):

            new_process = processes[index]

            update_process_state(new_process, "READY")

            log_event(
                f"[TIME {time}] Process {new_process['pid']} entered READY state"
            )

            queue.append(new_process)

            index += 1

        # Process completed
        if remaining[process["pid"]] == 0:

            completion = time

            tat = (
                completion
                - process["arrival_time"]
            )

            wt = (
                tat
                - process["burst_time"]
            )

            rt = (
                start
                - process["arrival_time"]
            )

            update_process_state(process, "TERMINATED")

            log_event(
                f"[TIME {time}] Process {process['pid']} TERMINATED"
            )

            results.append({
                "pid": process["pid"],
                "arrival_time": process["arrival_time"],
                "burst_time": process["burst_time"],
                "completion_time": completion,
                "turnaround_time": tat,
                "waiting_time": wt,
                "response_time": rt,
                "state": process["state"]
            })

        else:

            update_process_state(process, "READY")

            log_event(
                f"[TIME {time}] Process {process['pid']} returned to READY state"
            )

            queue.append(process)

    return results, gantt