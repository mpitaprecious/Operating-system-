from collections import deque

from utils.pcb import update_process_state
from utils.logger import log_event



# FIRST COME, FIRST SERVED (FCFS)

def fcfs(processes):

    print("FCFS started")

    processes = sorted(
        processes,
        key=lambda x: (
            x["arrival_time"],
            x["pid"]
        )
    )

    time = 0

    results = []
    gantt = []

    for process in processes:

        # CPU idle handling
        if time < process["arrival_time"]:
            time = process["arrival_time"]

        update_process_state(process, "RUNNING")

        log_event(
            f"[TIME {time}] Process {process['pid']} entered RUNNING state"
        )

        start = time

        completion = start + process["burst_time"]

        tat = completion - process["arrival_time"]

        wt = tat - process["burst_time"]

        rt = start - process["arrival_time"]

        gantt.append(
            (
                process["pid"],
                start,
                completion
            )
        )

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

    return results, gantt


# SHORTEST JOB FIRST (SJF)
# NON-PREEMPTIVE

def sjf(processes):

    print("SJF started")

    processes = sorted(
        processes,
        key=lambda x: (
            x["arrival_time"],
            x["pid"]
        )
    )

    completed = []
    ready_queue = []
    gantt = []

    time = 0
    index = 0
    n = len(processes)

    while len(completed) < n:

        while (
                index < n
                and processes[index]["arrival_time"] <= time
        ):
            ready_queue.append(processes[index])
            index += 1

        # CPU idle
        if not ready_queue:

            if index < n:
                time = processes[index]["arrival_time"]

            continue

        ready_queue.sort(
            key=lambda x: (
                x["burst_time"],
                x["arrival_time"],
                x["pid"]
            )
        )

        process = ready_queue.pop(0)

        update_process_state(process, "RUNNING")

        log_event(
            f"[TIME {time}] Process {process['pid']} entered RUNNING state"
        )

        start = time

        completion = start + process["burst_time"]

        tat = completion - process["arrival_time"]

        wt = tat - process["burst_time"]

        rt = start - process["arrival_time"]

        gantt.append(
            (
                process["pid"],
                start,
                completion
            )
        )

        update_process_state(process, "TERMINATED")

        log_event(
            f"[TIME {completion}] Process {process['pid']} TERMINATED"
        )

        completed.append({
            "pid": process["pid"],
            "arrival_time": process["arrival_time"],
            "burst_time": process["burst_time"],
            "start_time": start,
            "completion_time": completion,
            "turnaround_time": tat,
            "waiting_time": wt,
            "response_time": rt,
            "state": process["state"]
        })

        time = completion

    return completed, gantt

# PRIORITY SCHEDULING
# NON-PREEMPTIVE WITH AGING

def priority_scheduling(processes):

    print("Priority Scheduling started")

    processes = sorted(
        processes,
        key=lambda x: (
            x["arrival_time"],
            x["pid"]
        )
    )

    completed = []
    ready_queue = []
    gantt = []

    time = 0
    index = 0
    n = len(processes)

    while len(completed) < n:

        while (
                index < n
                and processes[index]["arrival_time"] <= time
        ):

            process = processes[index].copy()

            process["current_priority"] = process["priority"]

            ready_queue.append(process)

            index += 1

        # CPU idle
        if not ready_queue:

            if index < n:
                time = processes[index]["arrival_time"]

            continue

        # Aging mechanism
        for process in ready_queue:

            waiting_time = time - process["arrival_time"]

            ageing_steps = waiting_time // 3

            improved_priority = (
                    process["priority"]
                    - ageing_steps
            )

            process["current_priority"] = max(
                0,
                improved_priority
            )

        ready_queue.sort(
            key=lambda x: (
                x["current_priority"],
                x["arrival_time"],
                x["pid"]
            )
        )

        process = ready_queue.pop(0)

        update_process_state(process, "RUNNING")

        log_event(
            f"[TIME {time}] Process {process['pid']} entered RUNNING state"
        )

        start = time

        completion = start + process["burst_time"]

        tat = completion - process["arrival_time"]

        wt = tat - process["burst_time"]

        rt = start - process["arrival_time"]

        gantt.append(
            (
                process["pid"],
                start,
                completion
            )
        )

        update_process_state(process, "TERMINATED")

        log_event(
            f"[TIME {completion}] Process {process['pid']} TERMINATED"
        )

        completed.append({
            "pid": process["pid"],
            "priority": process["current_priority"],
            "arrival_time": process["arrival_time"],
            "burst_time": process["burst_time"],
            "start_time": start,
            "completion_time": completion,
            "turnaround_time": tat,
            "waiting_time": wt,
            "response_time": rt,
            "state": process["state"]
        })

        time = completion

    return completed, gantt


# ROUND ROBIN (RR)
# PREEMPTIVE

def round_robin(processes, quantum=2):

    print("Round Robin started")

    processes = sorted(
        processes,
        key=lambda x: (
            x["arrival_time"],
            x["pid"]
        )
    )

    queue = deque()

    time = 0
    index = 0

    gantt = []
    results = []

    remaining = {}
    first_response = {}

    for process in processes:

        remaining[process["pid"]] = process["burst_time"]

        first_response[process["pid"]] = None

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

            if index < len(processes):
                time = processes[index]["arrival_time"]

            continue

        process = queue.popleft()

        update_process_state(process, "RUNNING")

        log_event(
            f"[TIME {time}] Process {process['pid']} entered RUNNING state"
        )

        start = time

        # Store first response only once
        if first_response[process["pid"]] is None:

            first_response[process["pid"]] = (
                    start
                    - process["arrival_time"]
            )

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

        # Add newly arrived processes
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

            rt = first_response[process["pid"]]

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