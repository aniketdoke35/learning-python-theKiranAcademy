cars = ["bmw","mahidra","suzuki","rolls royal","aston martin","tata","audi","mustang"];


print(cars.index("mustang"));

# List index() method searches for a given element from the start of the list and returns the position of the first occurrence.



cars.append("ferrari");
print(cars);

# Python list append() method is used to add elements at the end of the list.

cars.insert(3 ,"porsche");
print(cars);

# The sort() method in Python is a built-in function that allows us to sort the elements of a list in ascending or descending order

cars.sort();
print(cars);

# The sorted() function sorts an iterable, like a list, tuple, or string, and returns a new sorted list. Unlike the list.sort() method, which sorts the list in place, sorted() creates a new list without modifying the original iterable. It is particularly useful when we need a sorted result but do not want to alter the original data structure.

x = sorted(cars);
print(x);

# remove() method removes a given element from the list.


cars.remove("audi");
print(cars);


otherCars = ["tesla","nissan"];
cars.extend(otherCars);
print(cars);

# The Python List extend() method adds items of an iterable (list, tuple, dictionary, etc) at the end of a list.

cars.pop();
print(cars);

# The pop() method is used to remove an element from a list at a specified index and return that element. If no index is provided, it will remove and return the last element by default. This method is particularly useful when we need to manipulate a list dynamically, as it directly modifies the original list.

c = cars.count("bmw");
print(c);

# The count() method is used to find the number of times a specific element occurs in a list. It is very useful in scenarios where we need to perform frequency analysis on the data.



cars.clear();
print(cars);

#  Removes all elements from the list.





