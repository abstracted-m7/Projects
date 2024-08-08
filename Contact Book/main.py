import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

# File to store contact data
CONTACT_FILE = 'contacts.csv'

# Check if the file exists; if not, create it
if not os.path.exists(CONTACT_FILE):
    with open(CONTACT_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone', 'Email', 'Address'])

# Function to load contacts from CSV
def load_contacts():
    contacts = []
    with open(CONTACT_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)
    return contacts

# Function to save contacts to CSV
def save_contacts(contacts):
    with open(CONTACT_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Phone', 'Email', 'Address'])
        writer.writeheader()
        writer.writerows(contacts)

# Function to add a new contact
def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contacts = load_contacts()
    contacts.append({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})
    save_contacts(contacts)

    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries()
    update_contact_list()

# Function to update the contact list display
def update_contact_list():
    contacts = load_contacts()
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to search for a contact
def search_contact():
    query = search_var.get()
    contacts = load_contacts()
    results = [contact for contact in contacts if query.lower() in contact['Name'].lower() or query in contact['Phone']]

    listbox.delete(0, tk.END)
    for contact in results:
        listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to load selected contact details into entry fields
def load_contact_details(event):
    selected = listbox.get(listbox.curselection())
    name, phone = selected.split(" - ")

    contacts = load_contacts()
    for contact in contacts:
        if contact['Name'] == name and contact['Phone'] == phone:
            name_var.set(contact['Name'])
            phone_var.set(contact['Phone'])
            email_var.set(contact['Email'])
            address_var.set(contact['Address'])
            break

# Function to update a contact
def update_contact():
    selected = listbox.get(listbox.curselection())
    if not selected:
        messagebox.showerror("Error", "No contact selected!")
        return

    name, phone = selected.split(" - ")

    contacts = load_contacts()
    for contact in contacts:
        if contact['Name'] == name and contact['Phone'] == phone:
            contact['Name'] = name_var.get()
            contact['Phone'] = phone_var.get()
            contact['Email'] = email_var.get()
            contact['Address'] = address_var.get()
            break

    save_contacts(contacts)
    messagebox.showinfo("Success", "Contact updated successfully!")
    clear_entries()
    update_contact_list()

# Function to delete a contact
def delete_contact():
    selected = listbox.get(listbox.curselection())
    if not selected:
        messagebox.showerror("Error", "No contact selected!")
        return

    name, phone = selected.split(" - ")

    contacts = load_contacts()
    contacts = [contact for contact in contacts if not (contact['Name'] == name and contact['Phone'] == phone)]
    save_contacts(contacts)

    messagebox.showinfo("Success", "Contact deleted successfully!")
    clear_entries()
    update_contact_list()

# Function to clear entry fields
def clear_entries():
    name_var.set('')
    phone_var.set('')
    email_var.set('')
    address_var.set('')

# Create main window
root = tk.Tk()
root.title("Contact Book")

# Create and place widgets
tk.Label(root, text="Name:").grid(row=0, column=0, padx=38, pady=5)
name_var = tk.StringVar()
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
phone_var = tk.StringVar()
tk.Entry(root, textvariable=phone_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
email_var = tk.StringVar()
tk.Entry(root, textvariable=email_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5)
address_var = tk.StringVar()
tk.Entry(root, textvariable=address_var).grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Search:").grid(row=5, column=0, padx=10, pady=5)
search_var = tk.StringVar()
tk.Entry(root, textvariable=search_var).grid(row=5, column=1, padx=10, pady=5)

tk.Button(root, text="Search", command=search_contact).grid(row=6, column=0, padx=10, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=6, column=1, padx=10, pady=5)

listbox = tk.Listbox(root, height=15, width=50)
listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
listbox.bind('<<ListboxSelect>>', load_contact_details)

# Load contacts initially
update_contact_list()

# Run the application
root.mainloop()
