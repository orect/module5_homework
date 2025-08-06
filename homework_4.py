def input_error(func):

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
    return wrapper

def get_contact(name, contacts):
    
    if name not in contacts:
        raise KeyError
    return contacts[name]

@input_error
def add_contact(args, contacts):
    name, phone = args  
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    get_contact(name, contacts)  
    contacts[name] = new_phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    (name,) = args  
    return get_contact(name, contacts)

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    command = parts[0].lower()
    arguments = parts[1:]
    return command, arguments

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    commands = {
        "add": lambda args: add_contact(args, contacts),
        "change": lambda args: change_contact(args, contacts),
        "phone": lambda args: show_phone(args, contacts),
        "all": lambda args: show_all(contacts),
    }

    while True:
        user_input = input("Enter a command: ")
        command, arguments = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command in commands:
            print(commands[command](arguments))
        elif command == "":
            print("Invalid command.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
