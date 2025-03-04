#👉 Given a list nums = [5, 10, 15, 20, 25, 30, 35], use negative slicing to get the last 3 elements.

nums = [5, 10, 15, 20, 25, 30, 35]
print(nums[-3:])

#👉 Given a list fruits = ["apple", "banana", "cherry", "date", "elderberry"], use negative slicing to remove the last 2 elements and print the remaining list.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[-5:-2])

#👉 Given a list colors = ["red", "green", "blue", "yellow"], use negative slicing to reverse the list.
colors = ["red", "green", "blue", "yellow"]
print(colors[::-1])

#4️⃣ 👉 Given a list numbers = [10, 20, 30, 40, 50, 60, 70], use negative slicing to get the middle 3 elements (excluding the first and last 2 elements).
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[-5:-2])

#👉 Given a list letters = ["a", "b", "c", "d", "e", "f", "g"], use negative slicing to reverse the list but skip every other element.
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters[::-2])