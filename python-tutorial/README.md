# Task 1: Identifying the Positions of a Word in a Sentence
In this task, you are required to create a program that identifies all the positions where a word occurs in a sentence. The program will take a word as input, search for that word in the sentence without considering case sensitivity, and return the positions of all occurrences of the word.

# Task 2: Replace Words with Positions and Save to a File
Problem
You need to extend the program to replace each word in the sentence with its position in a unique list of words. Then, save the list of words and their positions in the sentence to a file.

# Number 2. Code and test a program to
- identify the individual words in a sentence and stare them in a list 
- create a list of positions for words in that list
- save these two lists as a single file or as separate files.

To address this task, I'll walk you through the solution where we:

Identify individual words in a sentence and store them in a list.
Create a list of positions for each word based on their position in the unique list of words.
Save these two lists (either as a single file or as separate files).
Steps:
List 1: A list of unique words (ignoring case) from the sentence.
List 2: A list of positions where each word from the sentence appears in the unique words list.
You will have the option to save these lists as either:

A single file containing both the lists.
Two separate files where each file contains one list.
Python Code Implementation:

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