def find_word_positions(sentence, word):
    # Convert the input word to lowercase for case-insensitive comparison
    word_lower = word.lower()

    # Split the sentence into individual words
    words = sentence.split()

    # Initialize an empty list to store positions
    positions = []

    # Loop through the words and check if each matches the input word
    for i in range(len(words)):
        # Convert each word in the sentence to lowercase for comparison
        if words[i].lower() == word_lower:
            positions.append(i + 1)  # Record the position (1-based index)

    # If positions are found, return them
    if positions:
        return f"The word '{word}' occurs at positions: {positions}"
    else:
        return f"The word '{word}' is not found in the sentence."

# Example usage
sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
word = "COUNTRY"
result = find_word_positions(sentence, word)
print(result)
