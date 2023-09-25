# wesleyroberson.github.io

# Background:
    # Those familiar with Harry Potter will know that students are sorted into four houses at the school Hogwarts: Gryffindor, Hufflepuff, Ravenclaw, or Slytherin.
    The popular, related website, wizardingworld.com (formerly pottermore.com), has a version of the sorting test to allow users to be sorted into a house like the characters from the series.
    How the test works is asking eight rounds of multiple choice questions.
    There are multiple possible questions per round, so the actual questions received in any single iteration of the test can vary. This can lead to different results.

# Project purpose:
    # To provide the same sorting test but all possible questions (twenty-four) and probabilistic analysis telling the user how often he or she receives each house.


# Pottermore Sorting Quiz weights.csv
    # csv file containing the respective weights added to score the user's answers. Each line contains a unique ID, round number, number of possible questions in the round, question number, question, and weights for each of the four houses

# questions_answers.txt
    # txt file containing the test's twenty-four questions and their answer choices, to be read in by the sorting_test.py program

# sorting_analysis.py
    # python program reading in the answer weights from the Pottermore Sorting Quiz weights.csv file and the user's answer choices from the txt file created by the sorting_interface.py program. Sums scores accordingly, calculates the result for every iteration of test questions, outputs the number of times and probability each result is achieved, and deposits this information in a table to be displayed by the sorting_interface.py program

# sorting_interface.py
    # python program setting up the GUI users see when running the sorting_test.py file, allowing them to choose answer choices and navigate between questions. Upon completing the questions, writes the user's answers to a txt file and calls the methods from the sorting_analysis.py program and ultimately display the results

# sorting_test.py
    # python program reading in the questions and answer choices, breaking them into each set of question-and-question's-answer-choices, and calling the Sorting class from the sorting_interface.py program
