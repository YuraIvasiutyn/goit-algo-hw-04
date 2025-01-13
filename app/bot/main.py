def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Invalid data format. Type 'change username phone'."


def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Invalid data format. Type 'change username phone'."
    if name in contacts:
        contacts[name] = phone
        return "Contact changes."
    else:
        return f"Not found name is {name} if you add new contact, please enter a command add username phone"


def get_all_contacts(contacts):
    if contacts:
        for key, value in contacts.items():
            print(f"Name {key.capitalize()}, phone number {value}")
    else:
        print("Not data. if you add new contact, please enter a command add username phone")


def delete_contact(name, contacts):
    try:
        del contacts[name[0]]
        return "Record deleted."
    except ValueError:
        return "Invalid data format. Type 'Delete username'."


def get_phone_number(args, contacts):
    try:
        return contacts[args[0]]
    except ValueError:
        return "Invalid data format. Type 'Phone username'."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
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
            get_all_contacts(contacts)
        elif command == "delete":
            print(delete_contact(args, contacts))
        elif command == "phone":
            print(get_phone_number(args, contacts))
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
