# First-Come, First-Served (FCFS) Scheduling Algorithm

# Function to calculate waiting time
def calculate_waiting_time(processes, n, burst_time, waiting_time):
    waiting_time[0] = 0
    for i in range(1, n):
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]

# Function to calculate turnaround time
def calculate_turnaround_time(processes, n, burst_time, waiting_time, turnaround_time):
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

# Function to calculate average waiting and turnaround times
def fcfs_scheduling():
    # Taking inputs
    num_processes = int(input("Enter number of processes: "))
    processes = list(range(1, num_processes + 1))
    burst_time = []
    
    for i in range(num_processes):
        bt = int(input(f"Enter burst time for process {i + 1}: "))
        burst_time.append(bt)
        
    waiting_time = [0] * num_processes
    turnaround_time = [0] * num_processes

    # Calculating waiting time and turnaround time
    calculate_waiting_time(processes, num_processes, burst_time, waiting_time)
    calculate_turnaround_time(processes, num_processes, burst_time, waiting_time, turnaround_time)

    # Displaying results
    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(num_processes):
        print(f"{processes[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    # Calculating average waiting and turnaround time
    avg_waiting_time = sum(waiting_time) / num_processes
    avg_turnaround_time = sum(turnaround_time) / num_processes
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Calling the function
fcfs_scheduling()
