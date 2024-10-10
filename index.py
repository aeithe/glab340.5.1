import random

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

def generate_target():
    target = random.sample(words, random.randint(2, 5))
    return target

def display_lists(current, target):
    print("current lists: ", current)
    print("target lists: ", target)

def manipulate_list(current):
    print("choose an operation: ")
    print("1. append a word to the end of the list")
    print("2. extend the list with another list")
    print("3. concatenate two elements in the list")
    print("4. traverse the list and view its elements")
    print("5. modify an element in the list")
    print("6. insert an element at a specific index in the list")
    print("7. pop an elemetn from the list")
    print("8. remove a specific element from the list")
    print("9. sort the list in ascending or descending order")
    choice = int(input("enter your choice: "))
    if choice == 1:
        word = input("Enter a word to append: ")
        current.append(word)
    elif choice == 2:
        other_list = input("Enter a comma-seperated list to extend with: ").split(",")
        current.extend(other_list)
    elif choice == 3:
        index1 = int(input("Enter the index of the first element: "))
        index2 = int(input("Enter the index of the second element: "))
        if index1 >= 0 and index1 < len(current) and index2 >= 0 and index2 < len(current):
            current[index1] += current[index2]
            del current[index2]
        else:
            print("Invalid index")
    elif choice == 4:
        print("List elements: ")
        for word in current:
            print(word)
    elif choice == 5:
        index = int(input("Enter the index of the element to modify: "))
        if index >= 0 and index < len(current):
            word = input("Enter the new word: ")
            current[index] = word
        else:
            print("invalid index")
    elif choice == 6:
        index = int(input("enter the index to insert at: "))
        if index >= 0 and index <= len(current):
            word = input("enter the new word: ")
            current.insert(index, word)
        else:
            print("invalid index")
    elif choice == 7:
        if len(current) > 0:
            word = current.pop()
            print("popped word: ", word)
        else:
            print("list is empty")
    elif choice == 8:
        word = input("enter a word to remove: ")
        if word in current:
            current.remove(word)
        else:
            print("word not found in list")
    elif choice == 9:
        ascending = input("sort in ascending order? (y/n) ").lower() == "y"
        current.sort(reverse=not ascending)
    else:
        print("invalid choice")
    return


