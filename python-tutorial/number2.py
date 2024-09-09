# NUMBER 2:
#     To address this task, I'll walk you through the solution where we:

# Identify individual words in a sentence and store them in a list.
# Create a list of positions for each word based on their position in the unique list of words.
# Save these two lists (either as a single file or as separate files).
# Steps:
# List 1: A list of unique words (ignoring case) from the sentence.
# List 2: A list of positions where each word from the sentence appears in the unique words list.
# You will have the option to save these lists as either:

# A single file containing both the lists.
# Two separate files where each file contains one list.
# Python Code Implementation:


def process_sentence(sentence):
    # Split the sentence into individual words
    words = sentence.split()

    # Initialize empty lists to store unique words and positions
    unique_words = []
    word_positions = []

    # Loop through each word in the sentence
    for word in words:
        # Convert the word to lowercase for uniformity
        word_lower = word.lower()

        # If the word is not in the unique_words list, add it
        if word_lower not in unique_words:
            unique_words.append(word_lower)

        # Append the position of the word in the unique_words list (1-based index)
        word_positions.append(unique_words.index(word_lower) + 1)

    return unique_words, word_positions

def save_to_files(unique_words, word_positions, single_file=False):
    if single_file:
        # Save both lists in a single file
        with open("words_and_positions.txt", "w") as f:
            # Write unique words
            f.write("Unique Words:\n")
            for i, word in enumerate(unique_words, 1):
                f.write(f"{i}: {word}\n")
            
            # Write word positions
            f.write("\nWord Positions:\n")
            f.write(" ".join(map(str, word_positions)))
    else:
        # Save unique words and positions in separate files
        with open("unique_words.txt", "w") as f1:
            for i, word in enumerate(unique_words, 1):
                f1.write(f"{i}: {word}\n")
        
        with open("word_positions.txt", "w") as f2:
            f2.write(" ".join(map(str, word_positions)))

# Example usage
sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
unique_words, word_positions = process_sentence(sentence)

# Save to a single file or separate files based on the requirement
save_to_files(unique_words, word_positions, single_file=True)  # Single file
# save_to_files(unique_words, word_positions, single_file=False)  # Separate files

# Print the result for validation
print("Unique Words:", unique_words)
print("Word Positions:", word_positions)
