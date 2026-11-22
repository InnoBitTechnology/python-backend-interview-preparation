#creating an initial list
numbers=[10,20,500]

def add_item(numbers):

    #printing the original list without any change
    print(numbers)

    #we appended the list and added the item to it. append add the item or another list at the end
    numbers.append(10000)
    #returning the list after alteration
    return numbers

#creating an initial list
numbers=[10,20,500]
#calling the function with passing the string as positional argument
print(add_item(numbers))
#as list is mutable so any changes to the list gets the original list object changed hence ever after creating global varibale of list and making changes inside the function made the list changed.
#which was not same in case of int which we did in program 5 as int in immutable so any changes to the variable basically was creating a new variable rather than changing the original variable.
print(numbers)