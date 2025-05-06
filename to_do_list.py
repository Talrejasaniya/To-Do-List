to_do=[]
def show_task():
    if not  to_do:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i,task in enumerate(to_do,1):
            print(i,"->",task)
def add_task():
    task=input("Enter your task->")
    to_do.append(task)
    print(to_do)
def delete_task():
    show_task()
    try:
        task_num=int(input("Enter the task number to delete task->"))
        remove=to_do.pop(task_num-1)
        print("Remove->",remove)
    except (IndexError,ValueError):
        print("Invalid task number.")
def main():
    while True:
        
        print("\n------TO-Do-App-------")
        print("1. Veiw Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
    
        choice=input("Enter your choice from options->")
        if choice == "1":
            show_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.Try again.")
main()
