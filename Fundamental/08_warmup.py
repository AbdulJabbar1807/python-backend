# Ball 1: Accessing & updating a dictionary (Just like JSON in FastAPI)
player = {"name": "Kohli", "runs": 82, "balls": 53}
# TODO: Add a new key "strike_rate" to player equal to (runs / balls) * 100 and print player
player["strike_rate"] = (player["runs"]/player["balls"])*100
print(player)

# Ball 2: Looping through key and value together using .items()
scores = {"Ali": 85, "Zaid": 60, "Omar": 92}
for name, score in scores.items():
    # TODO: Write an if-statement to print ONLY the names of people with score > 80
    if score > 80:
        print(name)


# Ball 3: Turning Ball 2 into a 1-line List Comprehension
# Formula: [expression for key, val in dict.items() if condition]
top_students = [name for name,score in scores.items() if score > 80] # TODO: Replace [] with the 1-line list comprehension from Ball 2
print(top_students)