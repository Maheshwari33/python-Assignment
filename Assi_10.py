import tkinter as tk
import webbrowser as wb

root = tk.Tk()

# Entry widget
entry = tk.Entry(root, font=("Times New Roman", 30), width=30)
entry.grid(row=0, column=0)

l1 = tk.Label(root, font=("Times New Roman", 20))
l1.grid(row=1, column=0)
def display():
    search = entry.get()
    print(search)
    if search:
        l1.config(text="Navigating to google...")
        
        wb.open(f"https://www.google.com/search?q={search}")
    else:
        print("Please enter something")

search_button = tk.Button(root, text="Search", font=("Times New Roman", 20),bg="red", activebackground="cyan", command=display)
search_button.grid(row=3, column=0)

close_button = tk.Button(root, text="Close", font=("Times New Roman", 20),bg="red", activebackground="cyan", command=root.destroy)
close_button.grid(row=6, column=0)
root.mainloop()