# Function to allocate memory to processes using the First Fit algorithm
def first_fit(block_sizes, process_sizes):
    # Initialize allocation list and record the initial sizes of each block for output
    allocation = [-1] * len(process_sizes)
    initial_block_sizes = block_sizes.copy()

    # Loop through each process to allocate it to the first-fit block
    for i in range(len(process_sizes)):
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                allocation[i] = j
                block_sizes[j] -= process_sizes[i]  # Reduce block size after allocation
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

# Call the first fit function
first_fit(block_sizes, process_sizes)
