# Create a python program to manage shopping list.
#  a. Take input from user
#  b. This process must not stop unless user enters nothing
#  c. Use functions/methods to manage each operation
#  d. Manage validations such as if the item not found
#  e. On 8th option display list in tabular format
#  Inputs:
# 1 Add an item
# 2 Add multiple items
# 3 Add an item at index +
# 4 Remove last added item
# 5 Remove an item with name
# 6 Remove all items/ Empty list
# 7 Replace an item with new item
# 8 Display list
shopping_list = []
print("Welcome to the Shopping List Manager")
print("Options:")
print("1: Add an item")
print("2: Add multiple items")
print("3: Add an item at index")
print("4: Remove last added item")
print("5: Remove an item with name")
print("6: Remove all items/Empty list")
print("7: Replace an item with new item")
print("8: Display list")
print("Press Enter without typing anything to exit.")

while True:
    option = input("\nSelect an Option: ")
    if option == "":
        break
    if option == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"Added: {item}")
    elif option == "2":
            items = input("Enter the items to add: ").split(',')
            shopping_list.extend(items)
            print(f"Added items: {', '.join(items)}")
    elif option == "3":
            index = int(input("Enter the index to add the item at: "))
            item = input("Enter the item to add: ")
            if item:
                shopping_list.insert(index, item)
                print(f"Added {item} at index {index}")
    elif option == "4":
            if shopping_list:
                removed_item = shopping_list.pop()
                print(f"Removed last item: {removed_item}")
            else:
                print("The list is already empty.")
    elif option == "5":
        item = input("Enter item name to remove from list: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed: {item}")
        else:
            print(f"{item} not present in list.")
    elif option == "6":
        shopping_list.clear()
        print("Emptied the list.")
    elif option == "7":
        old_item = input("Enter item to be removed: ")
        if old_item in shopping_list:
            new_item = input("enter new item to add: ")
            index = shopping_list.index(old_item)
            shopping_list[index] = new_item
            print(f"The {old_item} is replaced by {new_item}")
    elif option == "8":
        if shopping_list:
            print("Shopping List: ")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}, {shopping_list}")
        else:
            print("No item in list.")
    else:
        print("Please choose option between 1-8.")