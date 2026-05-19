import csv


def export_results(results, filename="results_report.csv"):

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "PID",
            "Arrival Time",
            "Burst Time",
            "Completion Time",
            "Turnaround Time",
            "Waiting Time",
            "Response Time",
            "State"
        ])

        for r in results:

            writer.writerow([
                r["pid"],
                r["arrival_time"],
                r["burst_time"],
                r["completion_time"],
                r["turnaround_time"],
                r["waiting_time"],
                r["response_time"],
                r["state"]
            ])

    print(f"\nReport exported to {filename}")