def fifo_page_replacement(pages, frames):
    page_faults = 0
    frame_list = []
    
    for page in pages:
        # Check if the page is already in frame
        if page not in frame_list:
            # If frame is full, remove the first page (FIFO)
            if len(frame_list) >= frames:
                frame_list.pop(0)
            # Add the new page to the frame
            frame_list.append(page)
            page_faults += 1
        # Print current status of frames
        print(f"Page {page}: {frame_list}")
    
    print(f"\nTotal Page Faults: {page_faults}")

# Input
pages = list(map(int, input("Enter the page reference string (space-separated): ").split()))
frames = int(input("Enter the number of frames: "))

# Function call
fifo_page_replacement(pages, frames)
