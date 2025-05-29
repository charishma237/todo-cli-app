class Task:
    def __init__(self,title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status =  "✅" if self.done else "❌"
        return f"{status} {self.title}"
    
class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
    
    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks found!")

        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")

    def mark_done(self,index):
        try:
            self.tasks[index - 1].mark_done()
        except IndexError:
            print("⚠️ Invalid task number!")
    
    def delete_task(self, index):
        try:
            del self.tasks[index - 1]
        except IndexError:
            print("⚠️ Invalid task number!")

def menu():
    print("\n📋 To-Do Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def main():
    app = ToDoApp()
    while True:  # Infinite loop until user exits
        menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                title = input("Enter task: ")
                app.add_task(title)
            elif choice == 2:
                app.view_tasks()
            elif choice == 3:
                idx = int(input("Enter task number to mark done: "))
                app.mark_done(idx)
            elif choice == 4:
                idx = int(input("Enter task number to delete: "))
                app.delete_task(idx)
            elif choice == 5:
                print("Goodbye 👋")
                break
            else:
                print("⚠️ Invalid option!")
        except ValueError:
            print("⚠️ Please enter a number!")

if __name__ == "__main__":
    main()