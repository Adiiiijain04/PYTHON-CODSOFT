import tkinter as aditya
from tkinter import messagebox
from tkcalendar import Calendar

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        
        self.tasks = []

        self.task_entry = aditya.Text(master, width=40, height=5, font=('Helvetica', 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=5, sticky='ew')

        self.add_button = aditya.Button(master, text="Add Task", command=self.add_task, font=('Helvetica', 10, 'bold'))
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_listbox = aditya.Listbox(master, width=50, font=('Helvetica', 12))
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

        scrollbar = aditya.Scrollbar(master, orient="vertical", command=self.task_listbox.yview)
        scrollbar.grid(row=1, column=2, sticky='ns')
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        min_height = self.get_min_listbox_height(6)
        self.task_listbox.config(height=min_height)

        self.delete_button = aditya.Button(master, text="Delete Task", command=self.delete_task, font=('Helvetica', 10, 'bold'))
        self.delete_button.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        self.update_button = aditya.Button(master, text="Update Task", command=self.update_task, font=('Helvetica', 10, 'bold'))
        self.update_button.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        self.due_date_button = aditya.Button(master, text="Add Due Date", command=self.add_due_date, font=('Helvetica', 10, 'bold'))
        self.due_date_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

        self.done_button = aditya.Button(master, text="Mark as Done", command=self.mark_as_done, font=('Helvetica', 10, 'bold'))
        self.done_button.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

        self.load_tasks()

        self.task_entry.bind("<Key>", self.resize_text_box)
        self.task_listbox.bind("<Configure>", self.resize_task_listbox)

    def update_task_listbox(self):
        self.task_listbox.delete(0, aditya.END)
        for index, task_data in enumerate(self.tasks, start=1):
            task = task_data["task"]
            due_date = task_data["due_date"]
            done = task_data["done"]
            if done:
                self.task_listbox.insert(aditya.END, f"{index}. {task} - Done")
                self.task_listbox.itemconfig(aditya.END, {'bg': '#90EE90'})
            elif due_date:
                task += " - Due: " + due_date
                self.task_listbox.insert(aditya.END, f"{index}. {task}")
            else:
                self.task_listbox.insert(aditya.END, f"{index}. {task}")

    def add_due_date(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            top = aditya.Toplevel(self.master)
            cal = Calendar(top, selectmode='day', date_pattern='yyyy-mm-dd')
            cal.pack(padx=10, pady=10)

            def set_due_date():
                due_date = cal.get_date()
                self.tasks[selected_index[0]]["due_date"] = due_date
                self.update_task_listbox()
                top.destroy()

            confirm_button = aditya.Button(top, text="Set Due Date", command=set_due_date, font=('Helvetica', 10, 'bold'))
            confirm_button.pack(pady=5)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.update_task_listbox()

    def add_task(self):
        task = self.task_entry.get("1.0", aditya.END).strip()
        if task:
            self.tasks.append({"task": task, "due_date": None, "done": False})
            self.update_task_listbox()
            self.task_entry.delete("1.0", aditya.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            updated_task = self.task_entry.get("1.0", aditya.END).strip()
            if updated_task:
                self.tasks[selected_index[0]]["task"] = updated_task
                self.update_task_listbox()
                self.task_entry.delete("1.0", aditya.END)
            else:
                messagebox.showwarning("Warning", "Please enter an updated task.")

    def resize_task_listbox(self, event):
        tasks_count = max(self.task_listbox.size(), 6)
        self.task_listbox.config(height=tasks_count)

    def mark_as_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks[selected_index[0]]["done"] = True
            self.update_task_listbox()

    def get_min_listbox_height(self, num_tasks):
        font_size = int(self.task_listbox.cget("font").split()[1])
        line_height = font_size + 4
        min_height = num_tasks * line_height
        return min_height

    def resize_text_box(self, event):
        text_lines = self.task_entry.get("1.0", aditya.END).count("\n") + 1
        self.task_entry.config(height=text_lines)

    def load_tasks(self):
        pass

def main():
    root = aditya.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
