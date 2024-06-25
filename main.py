from todo_list import ToDoList

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Mark Task Complete")
        print("6. Save Tasks to File")
        print("7. Load Tasks from File")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            index = int(input("Enter task index: "))
            new_description = input("Enter new description: ")
            todo_list.update_task(index, new_description)
        elif choice == '3':
            index = int(input("Enter task index: "))
            todo_list.delete_task(index)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            index = int(input("Enter task index: "))
            todo_list.mark_task_complete(index)
        elif choice == '6':
            filename = input("Enter filename: ")
            todo_list.save_to_file(filename)
        elif choice == '7':
            filename = input("Enter filename: ")
            todo_list.load_from_file(filename)
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
