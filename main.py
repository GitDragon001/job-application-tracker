import json
import os

FILE_NAME = "applications.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def add_application(data):
    company = input("Company: ")
    role = input("Role: ")
    status = input("Status (applied/interview/offer/rejected): ")
    deadline = input("Deadline: ")

    app = {
        "company": company,
        "role": role,
        "status": status,
        "deadline": deadline
    }

    data.append(app)
    save_data(data)
    print("Added.\n")

def view_applications(data):
    if not data:
        print("No applications.\n")
        return
    for i, app in enumerate(data):
        print(f"{i+1}. {app['company']} - {app['role']} | {app['status']} | {app['deadline']}")
    print()

def update_status(data):
    view_applications(data)
    if not data:
        return
    index = int(input("Select number: ")) - 1
    if 0 <= index < len(data):
        new_status = input("New status: ")
        data[index]["status"] = new_status
        save_data(data)
        print("Updated.\n")
    else:
        print("Invalid.\n")

def delete_application(data):
    view_applications(data)
    if not data:
        return
    index = int(input("Select number: ")) - 1
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
        print("Deleted.\n")
    else:
        print("Invalid.\n")

def filter_by_status(data):
    status = input("Enter status: ")
    filtered = [app for app in data if app["status"].lower() == status.lower()]
    if not filtered:
        print("No matches.\n")
        return
    for app in filtered:
        print(f"{app['company']} - {app['role']} | {app['status']} | {app['deadline']}")
    print()

def menu():
    data = load_data()
    while True:
        print("1. Add application")
        print("2. View all")
        print("3. Update status")
        print("4. Delete")
        print("5. Filter by status")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_application(data)
        elif choice == "2":
            view_applications(data)
        elif choice == "3":
            update_status(data)
        elif choice == "4":
            delete_application(data)
        elif choice == "5":
            filter_by_status(data)
        elif choice == "6":
            break
        else:
            print("Invalid.\n")

if __name__ == "__main__":
    menu()
