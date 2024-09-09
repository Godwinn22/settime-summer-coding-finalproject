Explanation:
process_sentence():
Takes a sentence as input and splits it into individual words.
Identifies unique words (case-insensitive) and stores them in a list.
Creates a list of positions that maps each word in the sentence to its index in the unique words list.
save_to_files():
Saves the lists to files. Depending on the single_file argument, it can either save both lists in one file or separate them into two files.
For a single file: It creates a file words_and_positions.txt that stores both the unique words and positions.
For separate files: It creates two files: unique_words.txt and word_positions.txt.
Example Output Files:
Single file words_and_positions.txt
yaml
Copy code
Unique Words:
1: ask
2: not
3: what
4: your
5: country
6: can
7: do
8: for
9: you

Word Positions:
1 2 3 4 5 6 7 8 9 1 3 9 6 7 8 4 5
Separate files:
unique_words.txt

makefile
Copy code
1: ask
2: not
3: what
4: your
5: country
6: can
7: do
8: for
9: you
word_positions.txt

Copy code
1 2 3 4 5 6 7 8 9 1 3 9 6 7 8 4 5
You can modify the single_file argument to True for a single file, or False to create two separate files as per your need.