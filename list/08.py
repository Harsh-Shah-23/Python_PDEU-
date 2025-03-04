from collections import deque

queue = deque()

while True:
    print("\nQueue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front Element")
    print("4. Display Queue")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the element to enqueue: ")
        queue.append(item)
        print(f"{item} added to the queue.")
    
    elif choice == 2:
        if queue:
            print(f"Dequeued element: {queue.popleft()}")
        else:
            print("Queue is empty.")
    
    elif choice == 3:
        if queue:
            print(f"Front element: {queue[0]}")
        else:
            print("Queue is empty.")
    
    elif choice == 4:
        if queue:
            print("Queue:", list(queue))
        else:
            print("Queue is empty.")
    
    elif choice == 5:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please try again.")
