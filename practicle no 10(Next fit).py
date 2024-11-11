# Function to allocate memory to processes using the Next Fit algorithm
def next_fit(block_sizes, process_sizes):
    # Initialize allocation list and record the initial sizes of each block for output
    allocation = [-1] * len(process_sizes)
    initial_block_sizes = block_sizes.copy()
    last_allocated_block = 0  # Start with the first block

    # Loop through each process to allocate it to the next-fit block
    for i in range(len(process_sizes)):
        allocated = False  # Flag to check if the process is allocated
        for j in range(last_allocated_block, len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                allocation[i] = j
                block_sizes[j] -= process_sizes[i]  # Reduce block size after allocation
                last_allocated_block = j  # Update the last allocated block
                allocated = True
                break
        
        # If not allocated, loop around to the earlier blocks
        if not allocated:
            for j in range(0, last_allocated_block):
                if block_sizes[j] >= process_sizes[i]:
                    allocation[i] = j
                    block_sizes[j] -= process_sizes[i]  # Reduce block size after allocation
                    last_allocated_block = j  # Update the last allocated block
                    break

    # Display allocation results in a table format
    print("\nProcess No.\tProcess Size\tBlock No.\tBlock Size Before\tBlock Size After")
    for i in range(len(process_sizes)):
        if allocation[i] != -1:
            block_no = allocation[i]
            print(f"{i+1}\t\t{process_sizes[i]}\t\t{block_no + 1}\t\t{initial_block_sizes[block_no]}\t\t\t{block_sizes[block_no]}")
        else:
            print(f"{i+1}\t\t{process_sizes[i]}\t\tNot Allocated\t\t--\t\t\t--")

# User input for memory blocks and process sizes
block_sizes = list(map(int, input("Enter memory block sizes separated by spaces: ").split()))
process_sizes = list(map(int, input("Enter process sizes separated by spaces: ").split()))

# Call the next fit function
next_fit(block_sizes, process_sizes)
