# Priority Scheduling (Non-Preemptive) Algorithm in Python

# Function to calculate waiting and turnaround times
def priority_scheduling(processes):
    n = len(processes)
    # Sort processes based on arrival time
    processes.sort(key=lambda x: x['arrival_time'])

    # Initialize variables
    current_time = 0
    completed = 0
    is_completed = [False] * n

    while completed != n:
        # Find all processes that have arrived by current_time and are not completed
        ready_queue = [i for i in range(n) if processes[i]['arrival_time'] <= current_time and not is_completed[i]]
        
        if ready_queue:
            # Select process with highest priority (lowest priority number)
            # If priorities are same, select the process with earlier arrival time
            highest_priority_index = ready_queue[0]
            for i in ready_queue:
                if processes[i]['priority'] < processes[highest_priority_index]['priority']:
                    highest_priority_index = i
                elif processes[i]['priority'] == processes[highest_priority_index]['priority']:
                    if processes[i]['arrival_time'] < processes[highest_priority_index]['arrival_time']:
                        highest_priority_index = i

            # If current_time is less than the arrival time of the selected process, jump to its arrival time
            if current_time < processes[highest_priority_index]['arrival_time']:
                current_time = processes[highest_priority_index]['arrival_time']

            # Calculate waiting time and turnaround time
            processes[highest_priority_index]['waiting_time'] = current_time - processes[highest_priority_index]['arrival_time']
            processes[highest_priority_index]['turnaround_time'] = processes[highest_priority_index]['waiting_time'] + processes[highest_priority_index]['burst_time']

            # Update current_time
            current_time += processes[highest_priority_index]['burst_time']

            # Mark as completed
            is_completed[highest_priority_index] = True
            completed += 1
        else:
            # If no process is ready, increment current_time
            current_time += 1

    return processes

# Function to take input from user
def take_input():
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(n):
        print(f"\nEnter details for Process {i+1}:")
        arrival_time = int(input("Arrival Time: "))
        burst_time = int(input("Burst Time: "))
        priority = int(input("Priority (lower number means higher priority): "))
        processes.append({
            'pid': f'P{i+1}',
            'arrival_time': arrival_time,
            'burst_time': burst_time,
            'priority': priority
        })
    return processes

# Function to display the results
def display(processes):
    print("\nProcess\tArrival Time\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    total_waiting_time = 0
    total_turnaround_time = 0
    for proc in processes:
        total_waiting_time += proc['waiting_time']
        total_turnaround_time += proc['turnaround_time']
        print(f"{proc['pid']}\t{proc['arrival_time']}\t\t{proc['burst_time']}\t\t{proc['priority']}\t\t{proc['waiting_time']}\t\t{proc['turnaround_time']}")

    n = len(processes)
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# Main function
def main():
    processes = take_input()
    scheduled_processes = priority_scheduling(processes)
    display(scheduled_processes)

if __name__ == "__main__":
    main()
