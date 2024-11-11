def lru_page_replacement(pages, frames):
    page_faults = 0
    frame_list = []
    
    for page in pages:
        # Check if the page is already in frame
        if page not in frame_list:
            # If frame is full, remove the least recently used page
            if len(frame_list) >= frames:
                frame_list.pop(0)
            # Add the new page to the frame
            frame_list.append(page)
            page_faults += 1
        else:
            # Page is in frame, move it to the most recent position
            frame_list.remove(page)
            frame_list.append(page)
        
        # Print current status of frames
        print(f"Page {page}: {frame_list}")
    
    print(f"\nTotal Page Faults: {page_faults}")

# Input
pages = list(map(int, input("Enter the page reference string (space-separated): ").split()))
frames = int(input("Enter the number of frames: "))

# Function call
lru_page_replacement(pages, frames)
