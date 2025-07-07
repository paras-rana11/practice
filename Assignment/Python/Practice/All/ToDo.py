# Task: Build a Simple To-Do List Manager
# Write a Python program that allows the user to:
# Add tasks to a to-do list.
# View all tasks.
# Remove a task by its number.
# Mark a task as completed.
# Quit the program.

class ToDo:

    def __init__(self):
        self.todo_list = {}
        self.is_completed = {}

    def addTask(self, title, description):
        if not title.strip():
            raise ValueError("Title cannot be empty")
        if title in self.todo_list:
            raise ValueError("Task with this title already exists")
        self.todo_list[title] = description
        self.is_completed[title] = False

    def removeTask(self, index):
        if not self.todo_list:
            raise ValueError("No tasks to remove")
        if not (0 <= index < len(self.todo_list)):
            raise ValueError("Invalid task number")
        title = list(self.todo_list.keys())[index]
        self.todo_list.pop(title)
        self.is_completed.pop(title)

    def viewTask(self):
        if not self.todo_list:
            print("\nNo tasks available\n")
            return
        print("\nYour Tasks:")
        for index, (key, val) in enumerate(self.todo_list.items()):
            status = "✓" if self.is_completed[key] else " "
            print(f"[{status}] {index}. {key}: {val}")
        print()

    def editTask(self, index, new_title, new_description):
        if not self.todo_list:
            raise ValueError("No tasks to edit")
        if not (0 <= index < len(self.todo_list)):
            raise ValueError("Invalid task number")
        if not new_title.strip():
            raise ValueError("Title cannot be empty")
        
        old_title = list(self.todo_list.keys())[index]
        if new_title != old_title and new_title in self.todo_list:
            raise ValueError("Task with this title already exists")
        
        was_completed = self.is_completed[old_title]
        self.todo_list.pop(old_title)
        self.is_completed.pop(old_title)
        self.todo_list[new_title] = new_description
        self.is_completed[new_title] = was_completed

    def markCompleted(self, index):
        if not self.todo_list:
            raise ValueError("No tasks to mark as completed")
        if not (0 <= index < len(self.todo_list)):
            raise ValueError("Invalid task number")
        title = list(self.todo_list.keys())[index]
        if self.is_completed[title]:
            raise ValueError("Task is already marked as completed")
        self.is_completed[title] = True


if __name__ == "__main__":
    print("\n\n================== Welcome To To-Do List App ==================== \n")
    todo = ToDo()
    while True:
        try:
            print(f"""
        =================== Menu ====================
        1. Add tasks to a to-do list.
        2. View all tasks.
        3. Remove a task by its number.
        4. Mark a task as completed.
        5. Edit a task.
        6. Quit the program.
        """)
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                try:
                    print("Enter Task Title:")
                    title = input().strip()
                    print("Enter Task Description:")
                    description = input().strip()
                    todo.addTask(title, description)
                    print("-> Task Added Successfully")
                except Exception as e:
                    print(f"-> Failed to add task: {str(e)}")
            elif choice == 2:
                try:
                    todo.viewTask()                    
                except Exception as e:
                    print(f"-> Failed to view tasks: {str(e)}")

            elif choice == 3:
                try:
                    print("Enter Task Number:")
                    number = int(input())
                    todo.removeTask(number)
                    print("-> Task Removed Successfully")
                except ValueError:
                    print("-> Please enter a valid number")
                except Exception as e:
                    print(f"-> Failed to remove task: {str(e)}")

            elif choice == 4:
                try:
                    print("Enter Task Number:")
                    number = int(input())
                    if 0 <= number < len(todo.todo_list):
                        todo.markCompleted(number)
                        print("-> Task marked as completed")
                        todo.viewTask()
                    else:
                        print("-> Invalid task number")
                except ValueError:
                    print("-> Please enter a valid number")
                except Exception as e:
                    print(f"-> Failed to mark task as completed: {str(e)}")
            elif choice == 5:
                try:
                    print("Enter Task Number:")
                    number = int(input())
                    print("Enter New Task Title (press Enter to keep current):")
                    new_title = input().strip()
                    print("Enter New Task Description (press Enter to keep current):")
                    new_description = input().strip()
                    
                    if 0 <= number < len(todo.todo_list):
                        current_title = list(todo.todo_list.keys())[number]
                        if not new_title:
                            new_title = current_title
                        if not new_description:
                            new_description = todo.todo_list[current_title]
                        
                        todo.editTask(number, new_title, new_description)
                        print("-> Task edited successfully")
                        todo.viewTask()
                    else:
                        print("-> Invalid task number")
                except ValueError as e:
                    print(f"-> {str(e)}")
                except Exception as e:
                    print(f"-> Failed to edit task: {str(e)}")
            elif choice == 6:
                print("\n-> Thank You For Using To-Do List App")
                print("\n-> See You Soon!\n")
                break
            else:
                print("Please enter a valid choice (1-6)")
            
        except ValueError:
            print("\nPlease enter a valid choice (1-5)")
            print("Press Enter to continue...")
            input()
        except KeyboardInterrupt:
            print("\n\nExiting the program...")
            break
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            print("Press Enter to continue...")
            input()
