Python Strings
1.	Why are Python strings immutable?
A.  strings are immutable which means we can't actually change the string but when we are changing the string the actually thing which is happening is that creating a new string instead. This immutablity makes tring usable and safe and makes it usful as key in dictinary which makes program performance well.
2.	What is the difference between split() and join()?
a: Split create separate list items from the string where as join combines strings together.
3.	What does the strip() method do?
a: strip removes the which spaces from the starting and ending of the string.
4.	What does [::-1] do?
a: reverse the string. which simply means iterating from the end.
5.	Why can string concatenation inside a loop be potentially expensive?
a: Repeated string concatenation in a loop can be inefficient because strings are immutable. Building a list and using "".join() is generally more efficient.
6.	What is a frequency map?
a: creating the dictionary having the occurance of each characters in a string.
7.	Why is a dictionary useful for counting characters?
a: it's by defauly case sesitive so check each characters significantly and with the nature of dict we have key and values so operations on it becomes much easier and helpful.
8.	What is an anagram?
a: two string have the same character irrective of their orders.
9.	How would you check whether two strings are anagrams?
a: we can create a freq. map for both the text and then can check the equeality of it to know if they are anagram.
10.	What is the two-pointer technique?
a: check and comparing the elements from both the end respectivily. like the first element with the last element then second element with the last second elemnts and so. midle element don't need any comparision
11.	When is the two-pointer technique useful?
Two pointer technique is usefull fro checking the palindrome, reversing sequence, comparing elements from opposite ends.
12.	What is the difference between == and is?
a: == checks the value where as is checks the obj.
13.	Why should you not use is to compare normal strings?
a: is basically check if both the variables are sharing the same obj. but incase when we check the normal strings whe usually checks the value not the obj.

14.	What is the time complexity of searching for a character in a string?
a: best case: o(1) and worst case o(n).

15.	What is the time complexity of text[::-1]?
a: o(n)
16.	What is the time complexity of building a frequency dictionary for a string of length n?
a: o(n)
17.	Why is the optimized Two Sum solution O(n)?
a: finding the difference of target and the index value and then checking in the remaining values.
18.	What is the difference between O(n) time/O(n) space and O(n²) time/O(1) space?
a: time o(n) is iterating though loop, 0(n) storing all the elelement of data collection,

19.	Explain the Best Time to Buy and Sell Stock approach.
a: Scan the prices once while maintaining the minimum price seen so far. For each price, calculate the profit if we sell today and update the maximum profit. This gives O(n) time and O(1) space.
20.	If an interviewer asks you to optimize an O(n²) solution, what should you look for?
a: I would look for repeated work, unnecessary nested loops, and whether a data structure such as a set or dictionary can provide faster lookup. I would also consider sorting, two pointers, sliding window, prefix sums, or maintaining information while scanning the data once.
