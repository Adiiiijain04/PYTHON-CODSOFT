import tkinter as tinkterr
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.length_label = tinkterr.Label(master, text="Enter the desired length of the password:")
        self.length_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.length_entry = tinkterr.Entry(master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=5)
        self.complexity_label = tinkterr.Label(master, text="Select complexity level:")
        self.complexity_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.complexity_var = tinkterr.StringVar(value="Medium")  
        self.complexity_radio_low = tinkterr.Radiobutton(master, text="Low", variable=self.complexity_var, value="Low")
        self.complexity_radio_low.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        self.complexity_radio_medium = tinkterr.Radiobutton(master, text="Medium", variable=self.complexity_var, value="Medium")
        self.complexity_radio_medium.grid(row=1, column=2, padx=10, pady=5, sticky='w')
        self.complexity_radio_high = tinkterr.Radiobutton(master, text="High", variable=self.complexity_var, value="High")
        self.complexity_radio_high.grid(row=1, column=3, padx=10, pady=5, sticky='w')
        self.generate_button = tinkterr.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=4, padx=10, pady=5)
        self.password_label = tinkterr.Label(master, text="")
        self.password_label.grid(row=3, column=0, columnspan=4, padx=10, pady=5)                                        

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                self.password_label.config(text="Please enter a positive integer for length.")
                return

            complexity = self.complexity_var.get()
            character_sets = [string.ascii_lowercase, string.ascii_uppercase, string.digits]

            if complexity == "Low":
                character_sets = character_sets[:2]
            elif complexity == "High":
                character_sets.append(string.punctuation)

            all_characters = ''.join(character_sets)
            password = ''.join(random.choice(all_characters) for _ in range(length))
            self.password_label.config(text=f"Generated Password: {password}")

        except ValueError:
            self.password_label.config(text="Invalid input. Please enter a valid integer for length.")

def main():
    root = tinkterr.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
