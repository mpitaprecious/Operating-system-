def log_event(message):
    with open("scheduler.log", "a") as file:
        file.write(message + "\n")

    print(message)
