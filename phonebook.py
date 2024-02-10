import os
import pickle

class Contact:
    """A class to represent a contact.

    Attributes:
    first_name (str): The first name of the contact.
    last_name (str): The last name of the contact.
    phone (str): The cell phone number of the contact.
    home_phone (str): The home phone number of the contact.
    work_phone (str): The work phone number of the contact.
    job (str): The job title of the contact.
    address (str): The address of the contact.
    email (str): The email address of the contact.
    facebook_id (str): The Facebook ID of the contact.
    telegram_id (str): The Telegram ID of the contact.
    instagram_id (str): The Instagram ID of the contact.
    """

    def __init__(
        self,
        first_name=None, last_name= None,
        phone= None, home_phone= None, work_phone= None,
        job= None, address= None, email= None,
        facebook_id= None, telegram_id= None, instagram_id= None
        ):
        """Initializes a Contact object with the given attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.job = job
        self.address = address
        self.email = email
        self.facebook_id = facebook_id
        self. telegram_id = telegram_id
        self.instagram_id = instagram_id
    def details(self):
        """Returns a string with the details of the contact.

        Returns:
        str: A string with the contact's name and other attributes.
        """

        contact_details = self.__str__()
        contact_details += f"\nPhone : {self.phone}" if self.phone else ''
        contact_details += f"\nHome phone : {self.home_phone}" if self.home_phone else ''
        contact_details += f"\nWork phone : {self.work_phone}" if self.work_phone else ''
        contact_details += f"\nJob : {self.job}" if self.job else ''
        contact_details += f"\nAddress : {self.address}" if self.address else ''
        contact_details += f"\nE-mail : {self.email}" if self.email else ''
        contact_details += f"\nFace book : {self.facebook_id}" if self.facebook_id else ''
        contact_details += f"\nTelegram : {self.telegram_id}" if self.telegram_id else ''
        contact_details += f"\nInstagram: {self.instagram_id}" if self.instagram_id else ''
        return contact_details
    def __str__(self):
        """Returns a string with the name of the contact.

        Returns:
        str: A string with the contact's first name and last name.
        """

        return f'{self.first_name} {self.last_name}'

class Phonebook:
    """A class to represent a phonebook.

    Attributes:
    database_path (str): The path of the file where the contacts are stored.
    contacts (list): A list of Contact objects in the phonebook.
    selected_contact (int): The index of the currently selected contact in the list.
    """

    def __init__(self):
        """Initializes a Phonebook object with the given attributes.

        Loads the contacts from the file if it exists, or creates an empty list otherwise.
        Sets the selected contact to None.
        """

        self.database_path ='contacts.pickle'
        if not os.path.isfile(self.database_path):
            with open(self.database_path, 'wb') as f:
                pickle.dump([], f)
        with open(self.database_path, 'rb') as f:
            self.contacts = pickle.load(f)
        self.selected_contact = None
    def add(self, contact):
        """Adds a contact to the phonebook.

        Args:
        contact (Contact): The contact to be added.
        """

        self.contacts.append(contact)
    def save(self):
        """Saves the contacts to the file."""
        with open(self.database_path, 'wb') as f:
            pickle.dump(self.contacts, f)
    def delete(self):
        """Deletes the selected contact from the phonebook."""
        del self.contacts[self.selected_contact]
    def find(self, search_turm):
        """Find contacts with search terms in their names.

        Args:
        search_turm (str): The turm to be searched.

        Returns:
        list: A list of tuples containing the index and the contact object of the matching contacts.
        """

        found_contacts = []
        for i, c in enumerate(self.contacts):
            if search_turm in c.first_name or search_turm in c.last_name:
                found_contacts.append((i,c))
        return found_contacts
    def edit(self, edited_contact):
        """Edits the selected contact with the given contact.

        Args:
        edited_contact (Contact): The contact with the updated attributes.
        """

        self.contacts[self.selected_contact] = edited_contact
    def sort(self):
        """Sorts the contacts by their names."""
        self.contacts = sorted(self.contacts, key= lambda x: x.first_name+ x.last_name)
    def select_str(self):
        """Returns a string with the list of contacts and their numbers.

        Returns:
        str: A string with the contacts' names and numbers, with an asterisk for the selected contact.
        """

        contacts = ''
        for i, c in enumerate(self.contacts):
            contacts += f"[{'*' if self.selected_contact == i else ''}{i + 1}] {c.__str__()}\n"
        return contacts
    def length(self):
        """Returns the number of contacts in the phonebook.

        Returns:
        int: The number of contacts in the phonebook.
        """

        return len(self.contacts)
    def active_contact(self):
        """Returns the selected contact object.

        Returns:
        Contact: The selected contact object.
        """

        return self.contacts[self.selected_contact]
    def __str__(self):
        """Returns a string with the names of all the contacts.

        Returns:
        str: A string with the contacts' names separated by newlines.
        """

        return '\n'.join([c.__str__() for c in self.contacts])