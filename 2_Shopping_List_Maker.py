#Task 1: Write a function that lets the user add items to a list until the user replies "stop", and then returns the shopping list. 
#Task 2: Include a feature to remove items from the list. 
#Task 3: Add a feature that prints out the entire list in a formatted way.

# a shopping list
list = ["cereal", "bread", "sugar", "oatmeal", "noodles", "rice", "spaghetti", "apple juice", "coffee", "beef steaks", "salmon"]
 
while True:
    a = input("Do you want to add an item? 'add', 'remove' or 'stop' ?")
    if a == 'add':
        item = input("Enter the item you want to add: ")
        list.append(item)
        print(list)
  
    elif a == 'remove':
       item = input("Enter the item you want to remove: ")
       list.remove(item)
       print(list)
    
    elif a == 'stop':
       break

for item in list:
    print("- " + item)



    


    