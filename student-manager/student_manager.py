import json
import os

DB = "students.json"

def load():
    if not os.path.exists(DB):
        return []
    with open(DB, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save(data):
    with open(DB, "w") as f:
        json.dump(data, f, indent=2)

def add_student():
    data = load()
    sid = input("Student ID: ").strip()
    name = input("Name: ").strip()
    course = input("Course: ").strip()
    marks = input("Marks (comma separated): ").strip()
    marks_list = [float(x) for x in marks.split(",") if x.strip()]
    data.append({"id": sid, "name": name, "course": course, "marks": marks_list})
    save(data)
    print("Added.")

def list_students():
    for s in load():
        print(f"{s['id']} | {s['name']} | {s['course']} | {s['marks']}")

def find_student():
    key = input("Enter ID or name to search: ").strip().lower()
    for s in load():
        if key == s['id'].lower() or key in s['name'].lower():
            print(s)
            return
    print("Not found.")

def delete_student():
    data = load()
    sid = input("Student ID to delete: ").strip()
    new = [s for s in data if s['id'] != sid]
    if len(new) == len(data):
        print("ID not found.")
    else:
        save(new)
        print("Deleted.")

def average_marks():
    for s in load():
        marks = s.get("marks", [])
        avg = sum(marks)/len(marks) if marks else 0
        print(f"{s['id']} | {s['name']} | Average: {avg:.2f}")

def menu():
    actions = {
        "1": ("Add student", add_student),
        "2": ("List students", list_students),
        "3": ("Search student", find_student),
        "4": ("Delete student", delete_student),
        "5": ("Show averages", average_marks),
        "0": ("Exit", lambda: exit(0))
    }
    while True:
        for k,v in actions.items():
            print(k, "-", v[0])
        choice = input("Choice: ").strip()
        if choice in actions:
            actions[choice][1]()
        else:
            print("Invalid.")

if __name__ == "__main__":
    menu()
