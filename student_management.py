
import csv
import json
import logging
import os

logging.basicConfig(
    filename="student_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

CSV_FILE = "students.csv"
JSON_FILE = "students.json"

class StudentNotFoundError(Exception):
    pass

def initialize_files():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            csv.writer(f).writerow(["RegNo","Name","Age"])
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE,"w") as f:
            json.dump({}, f, indent=4)

def load_details():
    try:
        with open(JSON_FILE,"r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("JSON file is corrupted.")
        return {}
    except FileNotFoundError:
        return {}

def save_details(data):
    with open(JSON_FILE,"w") as f:
        json.dump(data,f,indent=4)

def add_student():
    try:
        reg=input("Registration Number: ").strip()
        name=input("Name: ").strip()
        age=int(input("Age: "))
        address=input("Address: ")
        contact=input("Contact: ")
        program=input("Program: ")

        with open(CSV_FILE,"a",newline="") as f:
            csv.writer(f).writerow([reg,name,age])

        details=load_details()
        details[reg]={"address":address,"contact":contact,"program":program}
        save_details(details)
        logging.info(f"Added {reg}")
        print("Student added successfully.")
    except ValueError:
        logging.error("Invalid age entered.")
        print("Age must be a number.")
    finally:
        print("Operation completed.\n")

def view_students():
    try:
        details=load_details()
        with open(CSV_FILE,"r") as f:
            reader=csv.DictReader(f)
            found=False
            for row in reader:
                found=True
                extra=details.get(row["RegNo"],{})
                print("-"*40)
                print("RegNo:",row["RegNo"])
                print("Name:",row["Name"])
                print("Age:",row["Age"])
                print("Address:",extra.get("address",""))
                print("Contact:",extra.get("contact",""))
                print("Program:",extra.get("program",""))
            if not found:
                print("No students found.")
        logging.info("Viewed students")
    finally:
        print()

def search_student():
    try:
        reg=input("Enter Registration Number: ")
        details=load_details()
        with open(CSV_FILE,"r") as f:
            for row in csv.DictReader(f):
                if row["RegNo"]==reg:
                    print(row)
                    print(details.get(reg,{}))
                    logging.info(f"Searched {reg}")
                    return
        raise StudentNotFoundError("Student not found.")
    except StudentNotFoundError as e:
        logging.error(str(e))
        print(e)
    finally:
        print()

def update_student():
    try:
        reg=input("Registration Number to update: ")
        rows=[]
        found=False
        with open(CSV_FILE,"r") as f:
            reader=csv.DictReader(f)
            for row in reader:
                if row["RegNo"]==reg:
                    found=True
                    row["Name"]=input("New Name: ")
                    row["Age"]=input("New Age: ")
                rows.append(row)
        if not found:
            raise StudentNotFoundError("Student not found.")

        with open(CSV_FILE,"w",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=["RegNo","Name","Age"])
            writer.writeheader()
            writer.writerows(rows)

        details=load_details()
        details[reg]={
            "address":input("New Address: "),
            "contact":input("New Contact: "),
            "program":input("New Program: ")
        }
        save_details(details)
        logging.info(f"Updated {reg}")
        print("Updated successfully.")
    except StudentNotFoundError as e:
        logging.error(str(e))
        print(e)
    finally:
        print()

def delete_student():
    try:
        reg=input("Registration Number to delete: ")
        rows=[]
        found=False
        with open(CSV_FILE,"r") as f:
            reader=csv.DictReader(f)
            for row in reader:
                if row["RegNo"]==reg:
                    found=True
                else:
                    rows.append(row)
        if not found:
            raise StudentNotFoundError("Student not found.")

        with open(CSV_FILE,"w",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=["RegNo","Name","Age"])
            writer.writeheader()
            writer.writerows(rows)

        details=load_details()
        details.pop(reg,None)
        save_details(details)
        logging.info(f"Deleted {reg}")
        print("Deleted successfully.")
    except StudentNotFoundError as e:
        logging.error(str(e))
        print(e)
    finally:
        print()

def menu():
    initialize_files()
    while True:
        print(" Student Record Management System ")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice=input("Choose option: ")
        if choice=="1":
            add_student()
        elif choice=="2":
            view_students()
        elif choice=="3":
            search_student()
        elif choice=="4":
            update_student()
        elif choice=="5":
            delete_student()
        elif choice=="6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__=="__main__":
    menu()
