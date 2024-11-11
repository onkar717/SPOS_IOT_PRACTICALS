# Shortest Job First (SJF) CPU Scheduling Algorithm

# Get the number of processes from the user
num_processes = int(input("Enter the number of processes: "))

# Initialize lists to store process information
processes = []
burst_times = []

# Take burst time input for each process
for i in range(num_processes):
    burst_time = int(input(f"Enter burst time for process {i + 1}: "))
    burst_times.append((burst_time, i + 1))  # store (burst_time, process_id) for sorting
    processes.append(i + 1)

# Sort processes by burst time
burst_times.sort()

# Initialize variables for calculating waiting and turnaround times
waiting_time = 0
turnaround_time = 0
total_waiting_time = 0
total_turnaround_time = 0

print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for burst_time, process_id in burst_times:
    # Calculate turnaround time for the process
    turnaround_time = waiting_time + burst_time
    total_turnaround_time += turnaround_time

    # Display process info
    print(f"P{process_id}\t{burst_time}\t\t{waiting_time}\t\t{turnaround_time}")

    # Update total waiting time and next waiting time
    total_waiting_time += waiting_time
    waiting_time += burst_time

# Calculate and display average waiting time and turnaround time
avg_waiting_time = total_waiting_time / num_processes
avg_turnaround_time = total_turnaround_time / num_processes

print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
