import matplotlib.pyplot as plt

# gantt_chart
def draw_gantt_chart(gantt):
    fig, ax = plt.subplots()

    colors = {
        1: "tab:blue",
        2: "tab:orange",
        3: "tab:green",
        4: "tab:red",
        5: "tab:purple"
    }

    y = 10

    for pid, start, end in gantt:
        ax.broken_barh(
            [(start, end - start)],
            (y, 5),
            facecolors=colors.get(pid, "tab:gray")
        )

        ax.text(
            start + (end - start) / 2,
            y + 2.5,
            f"P{pid}",
            ha='center',
            va='center',
            color='white'
        )

    ax.set_xlabel("Time")
    ax.set_ylabel("")
    ax.set_title("Round Robin Gantt Chart")

    ax.set_ylim(5, 20)

    ax.set_xlim(0, max(end for _, _, end in gantt) + 1)

    ax.set_yticks([])

    ax.grid(axis='x')

    plt.savefig("round_robin_gantt.png")

    plt.show()

    times = sorted(set(
        [start for _, start, _ in gantt] +
        [end for _, _, end in gantt]

    ))
    ax.set_xticks(times)

