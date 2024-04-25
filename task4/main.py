def parse_input(user_input):
    """
    This function parses usder input and return command and list of the arguments
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts:dict)->str:
    """
    This function adds contact to the contacts dictionary.
    Only unique contact name is available
    """
    if len(args) == 2: #function requires 2 arguments
        name, phone = args
        if not contacts.get(name): #trying to get contact from the dict
            contacts[name] = phone #adding new if not found
            return "Contact added."
        else:
            return "Cannot add contact. Contact with the same name already exists."
    else:
        return "Incorrect input format."

def change_contact(args,contacts:dict)->str:
    """
    This function cnahges existing contact.
    Returns an error if contact does not exist
    """
    if len(args) == 2:
        name, phone = args
        if contacts.get(name):
            contacts[name] = phone
            return "Contact updated."
        else:
            return f"Cannot update contact. Contact {name} does not exist."
    else:
        return "Incorrect input format."
    
def show_contacts(contacts:dict)->str:
    """
    This function returns contacts added to the dictionary
    """
    list_of_contacts=f"{'name':^10}{'phone':^10}\n"
    
    for name,phone in contacts.items():
        list_of_contacts+=f"{name:^10}{phone:^10}\n"
    
    return list_of_contacts
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()