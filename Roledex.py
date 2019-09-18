'''ICS 31 Lab6
Driver: UCI_ID: 20476591 Name: Sabrina Froehlich
Navigator: UCI_ID: 38916993 Name: Matthew Littman'''


def main():
    rolodex = {}
    default = "default.rol"
    while True:
        Intro_Message()
        command = input("Please Enter Your Command: ").lower()
        if command == "x":
            break
        default = Read_Command(command, rolodex, default)

class Contact:
    Name = None
    Phone_Number = None
    Email = None
    Note = None

def Read_Command(command: str, rolodex:dict, default:str):
    if command == "l":
        default = Load(rolodex,default)
        return default
    elif command == "i":
        Insert(rolodex,default)
        return default
    elif command == "r":
        Remove(rolodex, default)
        return default
    elif command == "f":
        Look_Up_Name(rolodex, default)
        return default
    elif command == "s":
        Save(rolodex,default)
        return default
    elif command == "n":
        Look_Up_Phone(rolodex, default)
        return default
    elif command == "e":
        Look_Up_Email(rolodex, default)
        return default
    elif command == "q":
        Quit_Save(rolodex,default)
    elif command == "p":
        Print_All (rolodex,default)
        return default
    else:
        print("Invalid command.")

def Intro_Message():
    print("\n")
    print("The Rolodex program allows editing of named Rolodex files.")
    print("If you specify a file that does not exist, the program will create it when saving.")
    print("Rolodex Commands: Insert(I), Remove(R), Lookup By Name(F), Lookup by Phone Number(N), Lookup by Email(E), Save(S), Quit and Save(Q), Print All(P), Quit and Don't Save(X)")


def Load(rolodex:dict,default:str)->str:
    current_default = "Rolodex name (current default is " + default + "): "
    rolodex_name = input(current_default)
    check = Check_File(rolodex_name)
    if rolodex_name == "":
        default = default
        file = open(default, "r")
    elif check == True:
        default = rolodex_name
        file = open(default,"r")
    elif check == False:
        print("Invalid file, opening default")
        file = open(default, "r")
    for line in file:
        name,phone,email,note = line.split("\t")
        rolodex[name] = Contact()
        rolodex[name].Name = name
        rolodex[name].Phone_Number = phone
        rolodex[name].Email = email
        rolodex[name].Note = note
    file.close()
    return default

def Check_File(rolodex_name: str) -> bool:
    try:
        file = open(rolodex_name, "r")
        file.close()
        return True
    except:
        return False

def Insert(rolodex: dict):
    name = input("Enter the Contact's Name: ")
    while Check_Name(name, rolodex) == True:
        print("Invalid value. Please try again.")
        name = input("Enter the Contact's Name: ")
    while name == "":
        print("Value needed. Please enter a name.")
        name = input("Enter the Contact's Name: ")
    number = input("Enter the Contact's Phone Number: ")
    while number == "":
        print("Value needed. Please enter a phone number.")
        number = input("Enter the Contact's Phone Number: ")
    email = input("Enter the Contact's Email: ")
    while email == "":
        print("Value needed. Please enter an email.")
        email = input("Enter the Contact's Email: ")
    note = input("Enter a Note about the Contact: ")
    rolodex[name] = Contact()
    rolodex[name].Name = name
    rolodex[name].Phone_Number = number
    rolodex[name].Email = email
    rolodex[name].Note = note

def Check_Name(name: str, rolodex: dict) -> bool:
    if name in rolodex:
        return True

def Remove(rolodex: dict):
    name = input("Enter the Name of the Contact, which you want to delete: ")
    if Check_Name(name,rolodex) != True:
        print("This contact does not exist.")
    else:
        del rolodex[name]
        print("Record Deleted.")

def Look_Up_Name(rolodex: dict, default:str):
    name = input("Enter the Name of the Contact, which you would like to look up: ")
    for c in rolodex.items():
        if c[0] == name:
            print("Name: ",c[0])
            print("Phone Number: ", rolodex[name].Phone_Number)
            print("Email: ",rolodex[name].Email)
            print("Note: ",rolodex[name].Note)
        elif c[0] not in rolodex:
            print("This contact does not exist")
    return default

def Look_Up_Phone(rolodex:dict, default:str):
    phone = input("Enter the Phone Number of the Contact, which you would like to look up: ")
    x = False
    for c in rolodex.items():
        name = c[0]
        if rolodex[name].Phone_Number == phone:
            print("Name: ", c[0])
            print("Phone Number: ", rolodex[name].Phone_Number)
            print("Email: ", rolodex[name].Email)
            print("Note: ", rolodex[name].Note)
            x = True
    if x == False:
        print("This contact does not exist")
    return default

def Look_Up_Email(rolodex:dict, default:str):
    email = input("Enter the Email of the Contact, which you would like to look up: ")
    x = False
    for c in rolodex.items():
        name = c[0]
        if rolodex[name].Email == email:
            print("Name: ", c[0])
            print("Phone Number: ", rolodex[name].Phone_Number)
            print("Email: ", rolodex[name].Email)
            print("Note: ", rolodex[name].Note)
            x = True
    if x == False:
        print("This contact does not exist")
    return default


def Save(rolodex:dict, default:str):
    current_default = "Save to Rolodex name (current default is " + default + "): "
    save_contacts = input(current_default)
    if save_contacts == "":
        file = open(default, "w")
    else:
        file = open(save_contacts, "w")
    print("Beginning Save")
    for name in rolodex:
        file.write(rolodex[name].Name + "\t" + rolodex[name].Phone_Number + "\t" + rolodex[name].Email + "\t" + rolodex[name].Note )
    print("Save Complete")
    file.close()
    return default

def Quit_Save(rolodex:dict, default:str):
    current_default = "Save to Rolodex name (current default is " + default + "): "
    save_contacts = input(current_default)
    if save_contacts == "":
        file = open(default, "w")
    else:
        file = open(save_contacts, "w")
    print("Beginning Save")
    for name in rolodex:
        file.write(rolodex[name].Name + "\t" + rolodex[name].Phone_Number + "\t" + rolodex[name].Email + "\t" + rolodex[
            name].Note)
    print("Save Complete")
    file.close()
    exit()

def Print_All(rolodex:dict, default:str):
    for c in rolodex.items():
        name = c[0]
        print("Name: ",c[0])
        print("Phone Number: ", rolodex[name].Phone_Number)
        print("Email: ",rolodex[name].Email)
        print("Note: ",rolodex[name].Note)
    return default

if __name__ == "__main__":
    main()

