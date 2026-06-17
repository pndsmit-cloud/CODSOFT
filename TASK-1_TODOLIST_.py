# this program is for making application of to do list using python
def main():
    print("Welcome to the To-Do List Application!")
    todo_list = []

    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.append(task)
            print(f"Task '{task}' added to the list.")
        elif choice == '2':
            if not todo_list:
                print("Your to-do list is empty.")
            else:
                print("Your tasks:")
                for index, task in enumerate(todo_list, start=1):
                    print(f"{index}. {task}")
        elif choice == '3':
            if not todo_list:
                print("Your to-do list is empty.")
            else:
                print("Your tasks:")
                for index, task in enumerate(todo_list, start=1):
                    print(f"{index}. {task}")
                task_number = int(input("Enter the number of the task to remove: "))
                if 1 <= task_number <= len(todo_list):
                    removed_task = todo_list.pop(task_number - 1)
                    print(f"Task '{removed_task}' removed from the list.")
                else:
                    print("Invalid task number.")
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")