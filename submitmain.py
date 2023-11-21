import json
import uuid
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def submit_anonymous_info():
    # Generate a unique identifier for each submission
    submission_id = str(uuid.uuid4())

    # Get current date and time
    submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get information from the user using a popup window
    info = tk.simpledialog.askstring("Input", "Enter your information:")

    # Create a dictionary to store the submission data
    submission_data = {
        "id": submission_id,
        "time": submission_time,
        "info": info
    }

    # Save the submission data to a file (you can modify this to store in a database)
    with open("anonymous_submissions.json", "a") as file:
        file.write(json.dumps(submission_data) + "\n")

    messagebox.showinfo("Success", "Submission successful. Your information has been submitted anonymously.")

class AnonymousInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Anonymous Information Submission App")

        # Create a button to submit information
        self.submit_button = tk.Button(root, text="Submit Information", command=self.submit_anonymous_info)
        self.submit_button.pack(pady=20)

        # Create a button to exit the app
        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack()

    def submit_anonymous_info(self):
        submit_anonymous_info()

if __name__ == "__main__":
    root = tk.Tk()
    app = AnonymousInfoApp(root)
    root.mainloop()
