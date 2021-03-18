# List examples
print("List examples")
print("Lists can contain different data types within the same list. Indexing starts from 0.")
listData = ["Beginning", 0, 1, 4 - 7j, 2, "End"]

# Outputting a full list
print("List: ", listData, "type :", type(listData))

# Referencing individual item by index
print("Individual item: listData[1]", listData[1])

# Slices of a list can be bounded or unbounded.
print("Bounded slice - listData[0:2]", listData[0:2])
print("Bounded slice - listData[3:]", listData[3:])
print("Bounded slice - listData[:3]", listData[:3])

print("See https://docs.python.org/3/library/functions.html#built-in-functions for details of other functions")