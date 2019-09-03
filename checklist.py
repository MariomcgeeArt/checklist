# my_fun_function = ("Hello World")
# print("Hello World")    


checklist = list()
# checklist



# # CREATE
def create(item):
    checklist.append(item)

# # READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    # index = 0
    for index, list_item in enumerate(checklist):        
        print("{} {}".format(index, list_item))
        # print(str(index) + list_item)
        # index += 1




# def mark_completed(index):
#     # add √ to checklist item   
#     #retrieve item form checklist ...add √ to item...print item + √
#     update(index, str('√') + item)    

    
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
        

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        read(int(item_index))

        # Remember that item_index must actually exist or our program will crash.
        # read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()


    # this may be the place where the code needs some restructering 
    
    elif function_code == "Q":
        # This is where we want to stop our loop
        return False
    ## indent may be needed 
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
    
    
    # create("purple sox")
    # create("red cloak")

    # print(read(0))
    # print(read(1))

    # update(0, "purple socks")
    # destroy(1)

    # print(read(0))

    select("C")
    list_all_items()

    select("R")
    list_all_items()


    select("P")
    list_all_items


    select("Q")
    list_all_items()
    # print(read(1))

    user_value = user_input("Please Enter a value:")
    print(user_value)



# checking save 


#test()


running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)
 