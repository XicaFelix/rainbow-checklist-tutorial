checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    checklist[index] = '√' + checklist[index]

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
        return True

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)
        return True
    # Print all items
    elif function_code == "P":
        list_all_items()
        return True
    # Catch all
    else:
        print("Unknown Option")
        return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def test():
    # Add your testing code here
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1))

    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()

    user_value = user_input("Please Enter a value:")
    print(user_value)

    test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)




