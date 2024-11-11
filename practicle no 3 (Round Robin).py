def round_robin(processes, burst_times, quantum):
    n = len(processes)
    remaining_burst = burst_times[:]
    waiting_times = [0] * n
    time = 0  # Current time

    while True:
        done = True
        for i in range(n):
            if remaining_burst[i] > 0:
                done = False
                if remaining_burst[i] > quantum:
                    time += quantum
                    remaining_burst[i] -= quantum
                else:
                    time += remaining_burst[i]
                    waiting_times[i] = time - burst_times[i]
                    remaining_burst[i] = 0
        if done:
            break

    turnaround_times = [waiting_times[i] + burst_times[i] for i in range(n)]
    
    # Calculating average waiting time and turnaround time
    avg_waiting_time = sum(waiting_times) / n
    avg_turnaround_time = sum(turnaround_times) / n

    # Displaying the results
    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t\t{burst_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# Input section
n = int(input("Enter number of processes: "))
processes = [input(f"Enter process ID for process {i + 1}: ") for i in range(n)]
burst_times = [int(input(f"Enter burst time for process {processes[i]}: ")) for i in range(n)]
quantum = int(input("Enter time quantum: "))

round_robin(processes, burst_times, quantum)
