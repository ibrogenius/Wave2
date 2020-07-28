#using the reverse() method
days = ['Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday']
days.reverse()
print(days)

#using the pop() method.. Eliminated 'Tuesday' because its at the index of 4
days = ['Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday']
days.pop(4)
print(days)

#using append() method
days = ['Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday']
days.append('Weekend')
print(days)

#using the clear() method
days = ['Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday']
days.clear()
print(days)

#using the copy() method
days = ['Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday']
days.copy()
print(days)

#using the count() method
days = ['Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday', 'Saturday']
day = days.count("Tuesday")
print(day)

#using the remove() method
days = ['Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday']
days.remove("Tuesday")
print(days)

#using the max() method for printing out the greatest element in the list
days = [1, 2, 3, 5, 9, 6, 7, 10]
max = max(days)
print(max)

#using the min() method for printing out the smallest element in the list
days = [1, 2, 3, 5, 9, 6, 7, 10]
min = min(days)
print(min)

#using sorted() method
days = [1, 2, 3, 5, 9, 6, 7, 10, 4, 8]
sort = sorted(days)
print(sort)

#using the .sort() method
days = [1, 2, 3, 5, 9, 6, 7, 10, 4, 8]
days.sort()
print(days)

#using the .len()
days = [1, 2, 3, 5, 9, 6, 7, 10, 4, 8]
length = len(days)
print(length)

#using the .join method()
name = "~~".join(["John", "Junior"])
print(name)