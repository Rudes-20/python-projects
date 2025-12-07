import json
import os
from datetime import datetime

DB = "expenses.json"

def load():
    if not os.path.exists(DB):
        return []
    with open(DB,"r") as f:
        try: return json.load(f)
        except: return []

def save(data):
    with open(DB,"w") as f:
        json.dump(data, f, indent=2)

def add_expense():
    data = load()
    amount = float(input("Amount: ").strip())
    cat = input("Category: ").strip()
    note = input("Note: ").strip()
    d = input("Date (YYYY-MM-DD) [enter for today]: ").strip() or datetime.today().strftime("%Y-%m-%d")
    data.append({"amount": amount, "category": cat, "note": note, "date": d})
    save(data)
    print("Saved.")

def monthly_report():
    data = load()
    month = input("YYYY-MM (e.g. 2025-01) [enter for current]: ").strip() or datetime.today().strftime("%Y-%m")
    filtered = [e for e in data if e["date"].startswith(month)]
    total = sum(e["amount"] for e in filtered)
    print("Total for", month, "=", total)
    by_cat = {}
    for e in filtered:
        by_cat[e["category"]] = by_cat.get(e["category"],0)+e["amount"]
    for k,v in by_cat.items():
        print(k, ":", v)

def list_all():
    for e in load():
        print(e)

def menu():
    actions = {"1":("Add expense", add_expense),
               "2":("Monthly report", monthly_report),
               "3":("List all", list_all),
               "0":("Exit", lambda: exit(0))}
    while True:
        for k,v in actions.items(): print(k,"-",v[0])
        c = input("Choice: ").strip()
        if c in actions: actions[c][1]()
        else: print("Invalid")

if __name__=="__main__":
    menu()
