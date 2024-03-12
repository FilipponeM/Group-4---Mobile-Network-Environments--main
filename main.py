import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel, Label, Entry, Checkbutton, Button

import os

# Global variable to store the logged-in username
logged_in_username = ""
class_code_verified = False


  # Function to handle registration
def register_account():
    global register_window  # Declare register_window as a global variable
    register_window = tk.Toplevel(login_window)
    register_window.title("Register Account")
    register_window.geometry('440x540')
    register_window.configure(bg='#333333')

    tk.Label(register_window, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
    new_username_entry = tk.Entry(register_window, font=("Arial", 16))
    new_username_entry.pack(pady=10)

    tk.Label(register_window, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
    new_password_entry = tk.Entry(register_window, show="*", font=("Arial", 16))
    new_password_entry.pack(pady=10)

    # Button to submit registration
    register_button = tk.Button(register_window, text="Register", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
                                    command=lambda: submit_registration(new_username_entry.get(), new_password_entry.get()))
    register_button.pack(pady=10)

# Function to handle login
def login():
    global logged_in_username, class_code_verified, class_code_window  # Include class_code_window in the list of global variables
    username = username_entry.get()
    password = password_entry.get()

    if is_valid_credential(username, password):
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        logged_in_username = username
        
        # Immediately prompt for class code verification
        if not class_code_verified:
            class_code_window = tk.Toplevel(login_window)
            class_code_window.title("Class Code Verification")
            class_code_window.geometry('500x400')
            class_code_window.configure(bg='#333333')

            tk.Label(class_code_window, text="Enter Class Name", bg='#333333', fg="#FFFFFF", font=("Arial",  16)).pack(pady=10)
            class_name_entry = tk.Entry(class_code_window, font=("Arial",  16))
            class_name_entry.pack(pady=10)

            tk.Label(class_code_window, text="Enter Passcode", bg='#333333', fg="#FFFFFF", font=("Arial",  16)).pack(pady=10)
            class_passcode_entry = tk.Entry(class_code_window, show="*", font=("Arial",  16))
            class_passcode_entry.pack(pady=10)

            submit_button = tk.Button(class_code_window, text="Submit", bg="#FF3399", fg="#FFFFFF", font=("Arial",  16),
                                      command=lambda: validate_class_details(class_name_entry.get(), class_passcode_entry.get()))
            submit_button.pack(pady=10)
            login_window.withdraw()

    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def validate_class_details(class_name, class_passcode):
    # Read the schoolCode.csv file and verify the class name and passcode
    filename = "schoolCode.csv"
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Class Name'] == class_name and row['Passcode'] == class_passcode:
                # Set class_code_verified to True since the class name and passcode are valid
                global class_code_verified
                class_code_verified = True
                
                # Destroy the class code window and proceed to the main page
                class_code_window.destroy()  # Correctly referencing the global variable
                main_page()  # This is called after the class code is verified
                return

    # If the loop completes without finding a match, show an error message
    messagebox.showerror(title="Error", message="Invalid class name or passcode.")


def upload_profile():
    global main_window
    upload_window = tk.Toplevel(main_window)
    upload_window.title("Upload Profile")
    upload_window.geometry('500x600')
    upload_window.configure(bg='#333333')
    
    # Adding input fields for profile information
    tk.Label(upload_window, text="First Name", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
    first_name_entry = tk.Entry(upload_window, font=("Arial", 16))
    first_name_entry.pack(pady=10)
    
    tk.Label(upload_window, text="Last Name", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
    last_name_entry = tk.Entry(upload_window, font=("Arial", 16))
    last_name_entry.pack(pady=10)
    
    tk.Label(upload_window, text="Bio", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
    bio_entry = tk.Text(upload_window, height=5, width=40, font=("Arial", 16))
    bio_entry.pack(pady=10)
    
    tk.Label(upload_window, text="Class", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
    class_entry = tk.Entry(upload_window, font=("Arial", 16))
    class_entry.pack(pady=10)
    
    # Submit button for profile creation
    submit_button = tk.Button(upload_window, text="Submit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
                              command=lambda: submit_profile(first_name_entry.get(), last_name_entry.get(), bio_entry.get("1.0", tk.END), class_entry.get()))
    submit_button.pack(pady=20)
    
def submit_profile(first_name, last_name, bio, class_name):
    # Fixed filename for saving all profiles
    filename = "_profile.csv"
    
    # Field names for the CSV file
    fieldnames = ['First Name', 'Last Name', 'Bio', 'Class']
    
    # Flag to check if profile already exists
    profile_exists = False
    

    with open(filename, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            'First Name': first_name,
            'Last Name': last_name,
            'Bio': bio,
            'Class': class_name
        })
        
        # Notify the user that the profile was uploaded
        messagebox.showinfo(title="Profile Uploaded", message="Your profile has been uploaded.")
   

    # Function to validate class details
    def validate_class_details(class_name, class_passcode):
        # Read the schoolCode.csv file and verify the class name and passcode
        filename = "schoolCode.csv"
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Class Name'] == class_name and row['Passcode'] == class_passcode:
                    # Set class_code_verified to True since the class name and passcode are valid
                    global class_code_verified
                    class_code_verified = True
                    
                    # Destroy the class code window and proceed to the main page
                    class_code_window.destroy()
                    main_page()  # This is called after the class code is verified
                    return


    # Function to handle registration
    def register_account():
        global register_window  # Declare register_window as a global variable
        register_window = tk.Toplevel(login_window)
        register_window.title("Register Account")
        register_window.geometry('440x540')
        register_window.configure(bg='#333333')

        tk.Label(register_window, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
        new_username_entry = tk.Entry(register_window, font=("Arial", 16))
        new_username_entry.pack(pady=10)

        tk.Label(register_window, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
        new_password_entry = tk.Entry(register_window, show="*", font=("Arial", 16))
        new_password_entry.pack(pady=10)

        # Button to submit registration
        register_button = tk.Button(register_window, text="Register", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
                                    command=lambda: submit_registration(new_username_entry.get(), new_password_entry.get()))
        register_button.pack(pady=10)

# Function to submit registration
def submit_registration(username, password):
    # Field names for the CSV file
    fieldnames = ['Username', 'Password']

    # Open the file in append mode ('a') and create a writer object
    with open('users.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the registration information as a dictionary
        writer.writerow({
            'Username': username,
            'Password': password
        })

    # Close the registration window
    if register_window:
        register_window.destroy()

    # Notify the user that the registration was successful
    messagebox.showinfo(title="Registration Successful", message="Your account has been registered. You can now log in.")

# Function to display the class code window
def show_class_code_window():
    global class_code_window
    class_code_window = tk.Toplevel(login_window)
    class_code_window.title("Class Code")
    class_code_window.geometry('300x200')
    class_code_window.configure(bg='#333333')

    tk.Label(class_code_window, text="Enter Class Code", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
    class_code_entry = tk.Entry(class_code_window, font=("Arial", 16))
    class_code_entry.pack(pady=10)

    tk.Label(class_code_window, text="Enter Class Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
    class_password_entry = tk.Entry(class_code_window, show="*", font=("Arial", 16))
    class_password_entry.pack(pady=10)

    submit_button = tk.Button(class_code_window, text="Submit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
                              command=lambda: validate_class_code(class_code_entry.get(), class_password_entry.get()))
    submit_button.pack(pady=10)

# Function to validate class code and password
def validate_class_code(code, password):
    filename = "schoolCode.csv"

    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Class Code'] == code and row['Password'] == password:
                    global class_code_verified
                    class_code_verified = True
                    # If class code and password are valid, proceed to the main page
                    class_code_window.destroy()
                    main_page()
                    return

        # If the loop completes, the class code and password are invalid
        messagebox.showerror(title="Error", message="Invalid class code or password.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Class code file not found.")

# Function to display the main page
def main_page():
    global login_window
    global main_window  # Declare main_window as global

    # Destroy the login window
    login_window.destroy()

    # Create a new window for the main page
    main_window = tk.Tk()
    main_window.title("Main Page")
    main_window.geometry('440x540')
    main_window.configure(bg='#333333')

    # Add widgets to the main page here
    welcome_label = tk.Label(
        main_window, text="Welcome to VoteEase", bg='#333333', fg="#FFFFFF", font=("Arial", 24))
    welcome_label.pack(padx=50, pady=50)

    # Voting Button
    voting_button = tk.Button(main_window, text="Vote", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=vote)
    voting_button.pack(pady=10)

    # Function to check if a profile already exists before uploading
    def check_if_profile_exists():
        # Define the filename based on the username
        filename = f"{logged_in_username}_profile.csv"

        # Check if the profile already exists
       
        upload_profile()
  
    # Upload Profile Button
    upload_profile_button = tk.Button(
        main_window, text="Upload Profile", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=check_if_profile_exists)
    upload_profile_button.pack(pady=10)

    # Edit Profile Button
    edit_profile_button = tk.Button(
        main_window, text="Edit Profile", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=edit_profile)
    edit_profile_button.pack(pady=10)


def vote():
    vote_window = Toplevel(main_window)
    vote_window.title("Vote")
    vote_window.geometry("1200x800")  # Adjusted size to  1200x800
    vote_window.configure(bg='#333333')  # Set background color to white

    # Group the labels and text boxes together using a frame
    info_frame = tk.Frame(vote_window, bg='#FFFFFF')
    info_frame.pack(pady=10)

    # Candidate's Full Name
    full_name_label = Label(info_frame, text="Full Name:", bg='#FFFFFF', fg="#000000")
    full_name_label.grid(row=0, column=0, sticky="W")
    full_name_entry = Entry(info_frame, state='readonly', textvariable=tk.StringVar(value="Owen Oliveira"), bg='#FFFFFF', fg="#000000")
    full_name_entry.grid(row=0, column=1, sticky="W")

    # Candidate's Bio
    bio_label = Label(info_frame, text="Bio:", bg='#FFFFFF', fg="#000000")
    bio_label.grid(row=1, column=0, sticky="W")
    bio_entry = Entry(info_frame, state='readonly', textvariable=tk.StringVar(value="Im a great leader!"), bg='#FFFFFF', fg="#000000")
    bio_entry.grid(row=1, column=1, sticky="W")

    # Candidate's Class
    class_label = Label(info_frame, text="Class:", bg='#FFFFFF', fg="#000000")
    class_label.grid(row=2, column=0, sticky="W")
    class_entry = Entry(info_frame, state='readonly', textvariable=tk.StringVar(value="Network Environment"), bg='#FFFFFF', fg="#000000")
    class_entry.grid(row=2, column=1, sticky="W")

    # Checkbox for selection
    select_checkbox = Checkbutton(info_frame, text="Select", bg='#FFFFFF', fg="#000000")
    select_checkbox.grid(row=3, column=0, sticky="W")

    # Configure the columns to stay together
    info_frame.grid_columnconfigure(0, weight=1)
    info_frame.grid_columnconfigure(1, weight=1)
    for i in range(4):  # Adjust the range based on the number of rows you'll end up using
        info_frame.grid_rowconfigure(i, weight=1)


    # Close Button
    Button(vote_window, text="Close", command=vote_window.destroy).pack()


def edit_profile():
    filename = "_profile.csv"

    try:
        # Explicitly specify the fieldnames to ensure correct mapping
        fieldnames = ['Username', 'First Name', 'Last Name', 'Bio', 'Class']
        with open(filename, 'r') as file:
            reader = csv.DictReader(file, fieldnames=fieldnames)
            user_profile = next((row for row in reader if row['Username'].strip().lower() == 'owen'), None)

            if user_profile is None:
                messagebox.showerror(title="Error", message="User profile not found.")
                return

            global main_window
            upload_window = tk.Toplevel(main_window)
            upload_window.title("edit_window")
            upload_window.geometry('500x600')
            upload_window.configure(bg='#333333')

            # Adding input fields for profile information
            tk.Label(upload_window, text="First Name", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
            first_name_entry = tk.Entry(upload_window, font=("Arial", 16))
            first_name_entry.insert(0, user_profile.get('First Name', ''))  # Set the value from CSV
            first_name_entry.pack(pady=10)

            tk.Label(upload_window, text="Last Name", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
            last_name_entry = tk.Entry(upload_window, font=("Arial", 16))
            last_name_entry.insert(0, user_profile.get('Last Name', ''))  # Set the value from CSV
            last_name_entry.pack(pady=10)

            tk.Label(upload_window, text="Bio", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
            bio_entry = tk.Text(upload_window, height=5, width=40, font=("Arial", 16))
            bio_entry.insert(tk.END, user_profile.get('Bio', ''))  # Set the value from CSV
            bio_entry.pack(pady=10)

            tk.Label(upload_window, text="Class", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
            class_entry = tk.Entry(upload_window, font=("Arial", 16))
            class_entry.insert(0, user_profile.get('Class', ''))  # Set the value from CSV
            class_entry.pack(pady=10)

            # Submit button for profile creation
            submit_button = tk.Button(upload_window, text="Submit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
                                      command=lambda: submit_profile(first_name_entry.get(), last_name_entry.get(), bio_entry.get("1.0", tk.END), class_entry.get()))
            submit_button.pack(pady=20)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Profile file not found.")
        
# Function to submit the edited profile
def submit_edited_profile(first_name, last_name, bio, class_name):
    # Define the filename for submitting the edited profile
    filename = f"{logged_in_username}_profile.csv"
    # Field names for the CSV file
    fieldnames = ['First Name', 'Last Name', 'Bio', 'Class']

    # Open the file in read mode ('r') and create a list to store rows
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # Open the file in write mode ('w') and create a writer object
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the updated profile information
        for row in rows:
            if row['First Name'] != '' and row['Last Name'] != '':
                row['Bio'] = bio
                row['Class'] = class_name

            # Write the row to the file
            writer.writerow(row)

    # Notify the user that the profile was updated
    messagebox.showinfo(title="Profile Updated", message="Your profile has been updated.")

    main_window.mainloop()

# Function to check credentials against CSV
def is_valid_credential(username, password):
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
    return False

# Initialize the login window
login_window = tk.Tk()
login_window.title("Login form")
login_window.geometry('440x540')
login_window.configure(bg='#333333')

# Creating widgets
login_label = tk.Label(
    login_window, text="Welcome to VoteEase", bg='#333333', fg="#FF3399", font=("Arial",  30))
username_label = tk.Label(
    login_window, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial",  16))
username_entry = tk.Entry(login_window, font=("Arial",  16))
password_entry = tk.Entry(login_window, show="*", font=("Arial",  16))
password_label = tk.Label(
    login_window, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial",  16))
login_button = tk.Button(
    login_window, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial",  16), command=login)

# Button for registering an account
register_button = tk.Button(
    login_window, text="Register Account", bg="#FF3399", fg="#FFFFFF", font=("Arial",  16), command=register_account)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
register_button.grid(row=4, column=0, columnspan=2, pady=10)

login_window.mainloop()