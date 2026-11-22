What is the difference between a parameter and an argument?
A: parameter can be defined as the variable defined in the function decleration whereas the argument is the actual value passed when the function is called. 

What are positional arguments?
a: based on the positions of the argument the value get assigned to. the variable (parameter) in declaration of function.

What are keyword arguments?
a: Actual value along with the variable names passed in the function call. those value get called with the variable name irrespective of the postion.

What are default arguments?
a: default argunments are the values which is defined to the parameters in the function declaration. those vale get overwritten when any another value passed in argument.

What is *args?
a: when we don't know how many positional arguments are being passed in the function called then we use *args.

What is **kwargs?
a: when we don't know how many keyword arguments are called during the function call then we use the keyword arguments.

What data type is args inside a function?
a: tuple

What data type is kwargs inside a function?
a: dict

What is local scope?
a: local variable defined inside the function.

What is global scope?
a: The variable defined outside the functions

Why should we avoid unnecessary global variables?
a: Functions that receive inputs and return outputs are easier to:
- test
- understand
- reuse
- debug

How does Python handle function arguments?
a: Python passes function arguments using a mechanism often called pass-by-object-reference. Python uses object reference/value semantics. Function arguments are references to objects. Mutating a mutable object inside the function can affect the caller's object, while rebinding the local parameter does not change the caller's variable.

Why can modifying a list inside a function affect the original list?
a: As list is mutable to any changes being done to the list actually modifies the original list unless changes done on a copy of the list.

Why doesn't rebinding an integer parameter affect the original integer?
a: As int is immutable hence when we say that we are modifying an int what actually we are doing is we are creating another obj hence the original number does not get effected.

What is a lambda function?
a: A lambda function is small function which is used for simple expressions.

What does enumerate() do?
a: it return the index and the value both.

What does zip() do?
a: it can combine two different type of collection data type and makes calling easies in single loop.

What is a list comprehension?
a: performing the list operations in single statement.

When should you avoid using a comprehension?
a: We should not use list comprehension when the complications gets high as in python readability matters.

Explain the sliding-window technique and why it can reduce an O(n×k) solution to O(n).
a: Sliding window technique is like calculating the first operation of window size then moving right by removing the left element and adding the right element. so the operation can be performed in single loop hence the compexity becomes o(n)