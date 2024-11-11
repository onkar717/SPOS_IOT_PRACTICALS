# Function to allocate memory to processes using the Best Fit algorithm
def best_fit(block_sizes, process_sizes):
    # Initialize allocation list and record the initial sizes of each block for output
    allocation = [-1] * len(process_sizes)
    initial_block_sizes = block_sizes.copy()

    # Loop through each process to allocate it to the best-fit block
    for i in range(len(process_sizes)):
        best_idx = -1  # Reset best index for each process

        # Find the best fit block for the current process
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                if best_idx == -1 or block_sizes[best_idx] > block_sizes[j]:
                    best_idx = j

        # If a suitable block is found, allocate it to the process
        if best_idx != -1:
            allocation[i] = best_idx
            block_sizes[best_idx] -= process_sizes[i]  # Reduce block size after allocation

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

# Call the best fit function
best_fit(block_sizes, process_sizes)
