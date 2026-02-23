
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


def main():
    student = input("type full name: ") 

    names, ranks, divs, ids = init_database()

    while True:
        choice = display_menu(student)

        if choice == "1":
            pass
        elif choice == "2":
            pass
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




