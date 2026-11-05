# Ball 1 (Dynamic Dict Fix): Add "role": "AI Engineer" to this dict on a NEW line using bracket notation
candidate = {"name": "Abdul", "city": "Hyderabad"}
# TODO: Write candidate[...] = ... below
candidate["role"] = "AI Engineer"
print(candidate)

# Ball 2 (String Cleaning): Strip the extra spaces and make this email all lowercase
raw_email = "   ABDUL.Backend@Gmail.COM   "
clean_email = raw_email.strip().lower()
print(clean_email)

# Ball 3 (String Splitting): Split this sentence into a list of words
sentence = "Never decide to give up"
words = sentence.split() # TODO: Use .split() on sentence
print(words)

# Ball 4 (List Indexing & Slicing): Print the FIRST word and the LAST word from 'words'
# Hint: index [0] is first, index [-1] is last
# TODO: print first and last word
print(words[0],words[-1])

# Ball 5 (List Append & Join): Add "ever" to the end of 'words' using .append(), then join them back with spaces
words.append("ever")
print(" ".join(words))