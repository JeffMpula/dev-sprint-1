def lookup_contact(contact_info):
    name = input("Enter contact name: ")

    if name in contact_info:
        print(f"{name}'s contact info is {contact_info[name]}")
    else:
        print("contact not found")
        return

def main():
    contact ={
        "Jeff":"0972652821",
        "Sharon":"097661010",
        "Andrew":"097896033"
    }

    lookup_contact(contact)

if __name__ == "__main__":
    main()