
def inti_database(): 

    names = ["Carol", "Jack", "Spock", "Hikaru", "Kira"]
    ranks = ["Captain", "Commander", "Lieutenant", "Major"]
    divs = ["Commander", "Officer", "Ambassador"]
    ids =["I01", "I02", "I03", "I04", "I05"]
    return names, ranks, divs, ids

def display_menu(): 
    student = input("type full name: ")
    print("logged in as:", student) 
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Display Roster")
    print("4. Search Crew")
    print("5. Update Rank")
    print("6. Exit")

def main():
    names, ranks, divs, ids = inti_database()
    while True:
        choice = diplay_menu()
        if choice == "1, 2, 3, 4, 5":
            pass
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

            main()  




