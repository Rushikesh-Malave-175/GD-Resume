'''GD-Resume-latest-Source.py - Created by Rushikesh-Malave-175, github (https://github.com/Rushikesh-Malave-175)'''


import tkinter as tk
import re
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext
import pyperclip
import webbrowser

def extract_file_id(link):
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', link)
    if match:
        return match.group(1)
    return None

def generate_link():
    drive_link = link_entry.get("1.0", tk.END).strip()
    file_id = extract_file_id(drive_link)
    if file_id:
        api_link = "https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&key=AIzaSyAv78uOOaUaNf6DWT59VUhZX7ZqnZDsY8k"
        api_link = api_link.replace("{file_id}", file_id)
        output_entry.configure(state='normal')
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, api_link)
        output_entry.configure(state='disabled')
    else:
        messagebox.showerror("Error", "Invalid Google Drive link")

def copy_to_clipboard():
    api_link = output_entry.get("1.0", tk.END).strip()
    pyperclip.copy(api_link)
    show_copy_message()

def open_link_in_browser():
    api_link = output_entry.get("1.0", tk.END).strip()
    webbrowser.open(api_link)
    show_filename_change_message()

def open_updates_page():
    webbrowser.open("https://github.com/Rushikesh-Malave-175/GD-Resume#getting-started")
    show_filename_change_message()

def open_support_page():
    webbrowser.open("https://www.buymeacoffee.com/rushikesh_m_175")
    show_filename_change_message()

def show_filename_change_message():
    filename_comment.configure(text="You might wanna rename the Downloaded file :)", fg="green")
    root.after(5000, clear_filename_change_message)

def clear_filename_change_message():
    filename_comment.configure(text="")

def show_copy_message():
    copy_comment.configure(text="Link copied to clipboard", fg="green")
    root.after(5000, clear_copy_message)

def clear_copy_message():
    copy_comment.configure(text="")

root = tk.Tk()
root.title("GD-Resume v2.0")

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate program size
program_width = int(screen_width * 0.4)
program_height = int(screen_height * 0.4)
program_x = (screen_width - program_width) // 2
program_y = (screen_height - program_height) // 2

# Set program size and position
root.geometry(f"{program_width}x{program_height}+{program_x}+{program_y}")

# Set the font size
font_size = 14  # Adjust the font size as per your preference

# Create label and entry for the Google Drive link
link_label = tk.Label(root, text="Paste your public Google Drive link here", font=("Arial", font_size))
link_label.pack()
link_entry = scrolledtext.ScrolledText(root, height=3, wrap=tk.WORD, font=("Arial", font_size))
link_entry.pack()

# Create the Generate button
generate_button = tk.Button(root, text="Generate", command=generate_link, height=1, font=("Arial", font_size))
generate_button.pack(pady=10)

# Create the output field
output_label = tk.Label(root, text="Generated Link:", font=("Arial", font_size))
output_label.pack()
output_entry = scrolledtext.ScrolledText(root, height=3, wrap=tk.WORD, state='disabled', font=("Arial", font_size))
output_entry.pack()

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create the Copy button
copy_button = tk.Button(button_frame, text="Copy link to Clipboard", command=copy_to_clipboard, height=1, font=("Arial", font_size))
copy_button.pack(side=tk.LEFT, padx=5)

# Create the "Open link in browser" button
open_link_button = tk.Button(button_frame, text="Open link in browser", command=open_link_in_browser, height=1, font=("Arial", font_size))
open_link_button.pack(side=tk.LEFT, padx=5)

# Create the "Check for updates" button
updates_button = tk.Button(button_frame, text="Check for updates", command=open_updates_page, height=1, font=("Arial", font_size))
updates_button.pack(side=tk.LEFT, padx=5)

# Create the "Support me here" button
support_button = tk.Button(button_frame, text="Support me here", command=open_support_page, height=1, font=("Arial", font_size))
support_button.pack(side=tk.LEFT, padx=5)

# Create a frame for the comments
comment_frame = tk.Frame(root)
comment_frame.pack()

# Create the filename change comment label
filename_comment = tk.Label(comment_frame, text="You might wanna rename the Downloaded file :)", fg="green", font=("Arial", font_size))
filename_comment.pack()

# Create the copy comment label
copy_comment = tk.Label(comment_frame, text="", fg="green", font=("Arial", font_size))
copy_comment.pack()

# Center align the comments
comment_frame.pack_configure(anchor='center')

root.mainloop()
