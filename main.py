
import csv

pokemons = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by text in name")
    print("5. Search by length of name")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # https://www.w3schools.com/python/python_lists_access.asp
        user_choice = int(input("Enter the pokemon's sequence number"))
        print(pokemons[user_choice])
        pass
    elif choice == '2':
        # https://www.w3schools.com/python/python_lists_sort.asp
        pokemons.sort()
        print(pokemons)
        pass
    elif choice == '3':
        # https://www.w3schools.com/python/python_lists_sort.asp
        pokemons.sort(reverse = True)
        print(pokemons)
        pass
    elif choice == '4':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/ref_string_startswith.asp
        user_choice2 = str(input("Enter the start of the pokemon's name"))
        newlist = []
        for x in pokemons:
            if user_choice2 in x:
                newlist.append(x)
        print(newlist)
    elif choice == '5':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        new_list2 = []
        user_choice3 = int(input("Enter the length of the pokemon's name"))
        new_list2 = [x for x in pokemons if len(x) == user_choice3]
        print(new_list2)
        pass
    elif choice == '6':
        start = 0
        print(pokemons[start:start + 10])
        user_choice4 = str(input("Enter n if you want to print the next 10 pokemons"))
        
    elif choice == '7':
        print(pokemons[-10:])
    elif choice == '8':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 6")

    print("==========================")
