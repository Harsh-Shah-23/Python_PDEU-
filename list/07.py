stack = []

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the element to push: ")
        stack.append(item)
        print(f"{item} pushed onto stack.")
    
    elif choice == 2:
        if stack:
            print(f"Popped element: {stack.pop()}")
        else:
            print("Stack is empty.")
    
    elif choice == 3:
        if stack:
            print(f"Top element: {stack[-1]}")
        else:
            print("Stack is empty.")
    
    elif choice == 4:
        if stack:
            print("Stack:", stack)
        else:
            print("Stack is empty.")
    
    elif choice == 5:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please try again.")
