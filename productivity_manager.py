#Date-Based Productivity & Expense Manager 
import json
try: 
    with open("tasks_data.json") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = {}    

def save_data():
    with open("tasks_data.json", "w") as file:
        json.dump(tasks, file, indent=4)



# 1. ADD TASKS
def add_tasks():
    print("\nOption number 1 selected successfully. Please enter a task to add")
    date = input("Please enter the date (DD-MM-YYYY): ").strip()
        
        
    if date not in tasks:
            tasks[date] = {"tasks" : [],
                           "expenses" : []
                           }
    print(f"\n\033[1mNow you can add tasks for {date}\033[0m.")   
    print("Type [DONE] when you want to stop adding.\n") 

    while True:
        task_name = input("Please enter the task to add to list: ")
        if task_name.lower() == "done":
                print("Tasks has been added successfully")
                break
        task = {
            "title" : task_name,
            "completed" : False
        }
            
        tasks[date]["tasks"].append(task)
        save_data()



# 2.VIEW TASKS
def view_tasks():
    print("\nOption number 2 selected successfully. Your tasks are listed down here") 
    date = input("Please enter the date (DD-MM-YYYY) to view task for that day: ")
    if date not in tasks or not tasks[date]:
        print("No tasks are available for this date")
    else:
        for index, task in enumerate(tasks[date]["tasks"], start=1):
            status = "✔" if task["completed"] else "✘"    
            print(f"{index}. {task['title']} : {status}")



# 3. MARK TASK AS COMPLETED
def mark_task_completed():
    print("\nOption number 3 selected successfully. Please mark a task as completed")
    date = input("Please enter the date (DD-MM-YYYY) whose task you want to mark as completed: ")
    if date not in tasks or not tasks[date]:
        print("No tasks available for this date to mark as complete")

    else:
        for index, task in enumerate(tasks[date]["tasks"], start=1):
                print(f"{index}. {task['title']}")   

        try:
            m = int(input("Please enter the task number you want to mark as completed: "))
            tasks[date]["tasks"][m - 1]["completed"] = True
            save_data()
            print("Task marked as complete successfully")
        except (ValueError, IndexError): 
            print("Invalid task number entered")



# 4. DELETE A TASK
def delete_task():
            print("\nOption number 4 selected successfully. Please delete a task")
            date = input("Please enter the date (DD-MM-YYYY) for which you want to delete a task: ")
            if date not in tasks or not tasks[date]:
                print("There are no tasks to be deleted")
            else:
                for index, task in enumerate(tasks[date]["tasks"], start=1):
                    print(f"{index}. {task['title']}")
                try:
                    delete_task = int(input("Please select the task number you want to delete: "))
                    tasks[date]["tasks"].pop(delete_task - 1)
                    save_data()
                    print("Task has been deleted successfully")
                except (ValueError, IndexError):
                    print("Invalid task number entered")



# 5. ADD EXPENSES
def add_expense():
    print("Option no. 5 selected to add expenses type ('done') to stop adding.")
    date = input("Please enter the date (DD-MM-YYYY): ").strip()

    if date not in tasks:
        tasks[date] = {"tasks" : [],
                           "expenses" : []
                           }  

    while True:
        category = input("Please enter the category the amount was spent upon: ")
        if category.lower() == "done":
                print("expenses have been added successfully") 
                break
        try:
            amount = float(input("Please enter the amount you spent: "))
                 
            expense = {
                    "category" : category,
                    "amount" : amount
                }
            tasks[date]['expenses'].append(expense)
            save_data()
        except ValueError:
            print("Invalid input entered in category or expense.")



# 6. VIEW EXPENSES
def view_expense():
    print("Option no. 6 selected to view expenses.")
    date = input("Please enter the date (DD-MM-YYYY): ")
    if date not in tasks or not tasks[date].get("expenses"):
        print("No expense has been added for this date.")
            

    for index, expense in enumerate(tasks[date]["expenses"], start=1):
        print(f"{index}. {expense['category']} : {expense['amount']}")



#7. SEE MONTHLY EXPENSES
def see_montly_expense():
    print("option no. 7 selected to view the total monthly expense.")
    month = input("Please enter the month (MM-YYYY): ").strip()

    total = 0
    for date in tasks:
        if date[3:] == month:

            for expense in tasks[date].get("expenses", []):
                total+= expense["amount"]

                 

    if total == 0 :
        print("no expense is added for this month")

    else:
        print(f"total expense for {month} is : {total}")



# 8. CLEAR THE DATA STORED IN JSON FILE
def clear_stored_tasks_and_expenses():
    confirm = input("Are you sure you want to delete all data? (yes/no): ")

    if confirm.lower() == "yes":
        tasks.clear()
        save_data()
        print("All data deleted successfully.")
    else:
        print("Operation cancelled.")



# 9. EXIT LOOP
def Exit():
        print("Exit successfull")

# 10. PRINT MENU 
def print_menu():
    print("\n\033[1mHEYY DEAR, Welcome to customisable to-do list\033[0m\n")
    print("PRESS: 1 -- To add a task.")
    print("PRESS: 2 -- To view all tasks.")
    print("PRESS: 3 -- Mark a task as completed.")
    print("PRESS: 4 -- Delete a task.")
    print("PRESS: 5 -- To add expenses.")
    print("PRESS: 6 -- To view expenses.")
    print("PRESS: 7 -- To see Total monthly expense.")
    print("PRESS: 8 -- To clear all data in storage.")
    print("PRESS: 9 -- Exit.\n")


while True:
    print_menu()

    
    try:
        n = int(input("GOOD DAY. Please enter your option number: ")) 
    except ValueError:
        print("Invalid input entered please enter a number between 1 - 9")    
        continue


    if n == 9:
        Exit()
        break   

    elif n == 8:
        clear_stored_tasks_and_expenses()

    elif n == 7:
        see_montly_expense()        

    elif n == 6:
        view_expense()

    elif n ==5:
        add_expense()   
                     
    elif n ==4:
        delete_task()     

    elif n ==3:
        mark_task_completed()   

    elif n ==2:
        view_tasks()
                

    elif n ==1:
        add_tasks()

    else:

        print("Invalid input please select a number between from 1 - 9")