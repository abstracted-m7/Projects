- Explanation

    Contact Storage:
        The contact details are stored in a CSV file (contacts.csv). The file includes the columns: Name, Phone, Email, and Address.
        If the file doesn't exist, it's created with the necessary headers.

    Functions:
        load_contacts: Reads contacts from the CSV file into a list of dictionaries.
        save_contacts: Writes the list of dictionaries back to the CSV file.
        add_contact: Adds a new contact to the list and saves it to the file.
        update_contact_list: Updates the display of contacts in the listbox.
        search_contact: Searches for contacts by name or phone number.
        load_contact_details: Loads the selected contact's details into the entry fields.
        update_contact: Updates the selected contact's details.
        delete_contact: Deletes the selected contact.
        clear_entries: Clears the input fields.

    GUI Components:
        Labels and entry fields for Name, Phone, Email, and Address.
        Buttons for adding, updating, searching, and deleting contacts.
        A listbox to display the contacts and allow selection for editing or deletion.
        Search functionality to filter contacts by name or phone number.

    Data Management:
        The contact details are managed through a CSV file, which ensures that the data persists between application runs.

    User Interaction:
        The user can add new contacts, search for specific contacts, update details of existing contacts, and delete contacts. The interface is designed to be intuitive, with clear labels and buttons for each action.

- Running the Application

    When the program is run, a window will appear where you can manage your contacts.
    The contacts are displayed in a list, and the user can perform all necessary operations through the provided buttons and input fields.