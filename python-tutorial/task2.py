def replace_words_with_positions(sentence):
    # Split the sentence into individual words
    words = sentence.split()

    # Initialize an empty list to store unique words
    unique_words = []

    # Initialize an empty list to store positions
    word_positions = []

    # Loop through each word in the sentence
    for word in words:
        # Convert the word to lowercase for uniformity
        word_lower = word.lower()

        # Add the word to unique_words if it is not already there
        if word_lower not in unique_words:
            unique_words.append(word_lower)

        # Record the position of the word in the unique_words list
        word_positions.append(unique_words.index(word_lower) + 1)

    # Write the unique words and positions to a file
    with open("word_data.txt", "w") as f:
        # Save the unique words list
        f.write("Unique Words:\n")
        for i, unique_word in enumerate(unique_words, 1):
            f.write(f"{i}: {unique_word}\n")

        # Save the word positions
        f.write("\nWord Positions:\n")
        f.write(" ".join(map(str, word_positions)))

    return unique_words, word_positions

# Example usage
sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
unique_words, word_positions = replace_words_with_positions(sentence)
print("Unique Words:", unique_words)
print("Word Positions:", word_positions)
