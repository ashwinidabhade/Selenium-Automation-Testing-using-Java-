import tkinter as tk
from tkinter import messagebox
import json
import os

def submit_form(data):
    with open("data/sample_input.json", "w") as f:
        json.dump(data, f)

    from automation.document_generator import generate_document
    generate_document(data)

    capture = messagebox.askyesno("Optional", "Do you want to take screenshots from app?")
    if capture:
        from automation.pq_generator import capture_screenshots
        capture_screenshots()

    messagebox.showinfo("Done", "PQ Document generated successfully.")

def launch_gui():
    window = tk.Tk()
    window.title("PQ Automation")

    entries = {}
    fields = ["Customer Name", "Address", "Email", "Contact", "Objective", "Calibrated Value", "Desired Value"]

    for field in fields:
        row = tk.Frame(window)
        label = tk.Label(row, text=field, width=20, anchor='w')
        entry = tk.Entry(row)
        row.pack(fill="x")
        label.pack(side="left")
        entry.pack(side="right", expand=True, fill="x")
        entries[field] = entry

    def on_submit():
        data = {key.replace(" ", "_").lower(): entry.get() for key, entry in entries.items()}
        submit_form(data)

    submit_btn = tk.Button(window, text="Generate PQ", command=on_submit)
    submit_btn.pack()
    window.mainloop()
