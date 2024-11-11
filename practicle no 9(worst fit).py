# Worst Fit Memory Allocation Algorithm

def worst_fit(blocks, m, processes, n):
    # Store the original memory sizes for later use in displaying the "before" memory
    original_blocks = blocks.copy()

    allocation = [-1] * n  # -1 means no allocation

    # For each process, find the largest block that can accommodate it
    for i in range(n):
        # Find the block with the maximum size that can fit the process
        max_index = -1
        for j in range(m):
            if blocks[j] >= processes[i]:  # Check if block can accommodate the process
                if max_index == -1 or blocks[j] > blocks[max_index]:  # Worst Fit Logic
                    max_index = j
        
        # If a block is found for the process
        if max_index != -1:
            allocation[i] = max_index  # Assign process to the block
            blocks[max_index] -= processes[i]  # Reduce the size of the block

    # Print the allocation result
    print("\nProcess No.\tProcess Size\tBlock No.\tBefore Memory\tRemaining Memory")
    for i in range(n):
        if allocation[i] != -1:
            print(f"{i + 1}\t\t{processes[i]}\t\t{allocation[i] + 1}\t\t{original_blocks[allocation[i]]}\t\t{blocks[allocation[i]]}")
        else:
            print(f"{i + 1}\t\t{processes[i]}\t\tNot Allocated\t\t-\t\t-")

# Take input from the user
m = int(input("Enter the number of memory blocks: "))
blocks = list(map(int, input("Enter the sizes of memory blocks: ").split()))
n = int(input("Enter the number of processes: "))
processes = list(map(int, input("Enter the sizes of processes: ").split()))

# Call the function to perform Worst Fit Allocation
worst_fit(blocks, m, processes, n)
