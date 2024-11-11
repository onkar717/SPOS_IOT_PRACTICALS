def optimal_page_replacement(pages, capacity):
    page_faults = 0
    page_frames = [-1] * capacity  # Initialize all frames with -1 (empty slots)

    for i in range(len(pages)):
        if pages[i] not in page_frames:
            if -1 in page_frames:
                # If there is an empty frame, place the page in it
                index = page_frames.index(-1)
                page_frames[index] = pages[i]
            else:
                # Find the page that will not be used for the longest period in the future
                future_occurrences = {page: float('inf') for page in page_frames}

                for j in range(i + 1, len(pages)):
                    if pages[j] in future_occurrences and future_occurrences[pages[j]] == float('inf'):
                        future_occurrences[pages[j]] = j
                
                page_to_replace = max(future_occurrences, key=future_occurrences.get)
                index = page_frames.index(page_to_replace)
                page_frames[index] = pages[i]

            print(f"Page {pages[i]} is loaded into memory.")
            page_faults += 1
        else:
            print(f"Page {pages[i]} is already in memory.")

    print(f"\nTotal Page Faults: {page_faults}")

# Accepting user input
page_references = list(map(int, input("Enter the page reference string (space-separated): ").split()))
memory_capacity = int(input("Enter the memory capacity (number of frames): "))

# Calling the function with user input
optimal_page_replacement(page_references, memory_capacity)
