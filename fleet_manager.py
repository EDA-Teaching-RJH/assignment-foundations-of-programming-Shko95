
def init_database(): 

    names = ["Carol", "Jack", "Shaxs", "Hikaru", "Kira"]
    ranks = ["Captain", "Captain" ,"Lieutenant", "Captain", "Colonel"]
    divs = ["Command", "Command","Security", "Command", "Command"]
    ids =["I01", "I02", "I03", "I04", "I05"]
    return names, ranks, divs, ids

def display_menu(student): 
    print("logged in as:", student) 
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Display Roster")
    print("4. Search Crew")
    print("5. Update Rank")
    print("6. Exit")

    choice = input("select option: ")
    return choice

def display_roster(names, ranks, divs, ids):
        print("Crew Roster:")
        print("Name / Rank / Division / ID")

        for i in range(len(names)):
            print(names[i], "/", ranks[i], "/", divs[i], "/", ids[i])

def search_by_id(ids, names, ranks, divs):
    Target = input("Enter ID to search: ")  

    found = False

    for i in range(len(ids)):
        if ids[i] == Target:
          print("Member Found:")
          print(names[i], "/", ranks[i], "/", divs[i], "/", ids[i])
          found = True

          if found == False:
            print("Member not found.")  

def remove_member(names, ranks, divs, ids):
    target = input("Enter ID to remove: ")

    for i in range(len(ids)):
        if ids[i] == target:
            del names[i]
            del ranks[i]
            del divs[i]
            del ids[i]
            print("Member removed.")
            return
    print("Member not found.")
        
def add_member(names, ranks, divs, ids):
    new_id = input("Enter new member ID: ")
    for exsisting_id in ids:
        if existing_id == new_id:
            print("ID already exists.")
            return
    new_name = input("Enter new member name: ")
    new_rank = input("Enter new member rank: ")
    new_div = input("Enter new member division: ")
    if new_rank not in ["Captain", "Lieutenant", "Colonel"]:
        print("Invalid rank.")
        return
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    print("Member added.")
    

def main():
    student = input("type full name: ") 

    names, ranks, divs, ids = init_database()

    while True:
        choice = display_menu(student)

        if choice == "1":
            add_member(names, ranks, divs, ids)
        elif choice == "2":
            remove_member(names, ranks, divs, ids)
        elif choice == "3":
            display_roster(names, ranks, divs, ids)
        elif choice == "4":
            search_by_id(ids, names, ranks, divs)
        elif choice == "5":
            pass
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
                
main()  




