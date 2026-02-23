
def init_database(): 

    names = ["Carol", "Jack", "Spock", "Hikaru", "Kira"]
    ranks = ["Captain", "Commander", "Lieutenant", "Major"]
    divs = ["Commander", "Officer", "Ambassador"]
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
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
                    
main()  




