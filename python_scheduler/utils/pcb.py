class ProcessControlBlock:

    def __init__(
        self,
        pid,
        arrival_time,
        burst_time,
        priority=0,

    ):

        self.pid = pid

        self.arrival_time = arrival_time

        self.burst_time = burst_time

        self.priority = priority

        self.remaining_time = burst_time

        self.completion_time = 0

        self.waiting_time = 0

        self.turnaround_time = 0

        self.response_time = -1

        self.state = "NEW"

    def to_dict(self):

        return {
            "pid": self.pid,
            "arrival_time": self.arrival_time,
            "burst_time": self.burst_time,
            "priority": self.priority,
            "completion_time": self.completion_time,
            "waiting_time": self.waiting_time,
            "turnaround_time": self.turnaround_time,
            "response_time": self.response_time,
            "state": self.state
        }


def update_process_state(process, new_state):
    process["state"] = new_state