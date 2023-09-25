# This file creates the interface for the user with the quiz questions
import tkinter as tk
from tkinter import ttk
from sorting_analysis import answers_and_weights
from sorting_analysis import separate_by_round
from sorting_analysis import get_all_score_combinations
from sorting_analysis import calculate_results
from sorting_analysis import max_value


class Sorting(tk.Tk):
    def __init__(self, question_blocks):
        super().__init__()

        self.question_blocks = question_blocks
        self.q_total = len(self.question_blocks)
        self.q_count = -1

        self.enter_label = None
        self.overview_label = None
        self.question_label = None
        self.empty_label = None
        self.results_message_label = None
        self.results_table_title_label = None

        self.text_box = None

        self.enter_button = None
        self.start_button = None
        self.previous_button = None
        self.next_button = None
        self.results_button = None

        self.radio_choice = None

        self.col_names = None
        self.tree = None
        self.table_data = None

        self.name = ''
        self.file_name = ''
        self.answer_file = ''

        self.answers = []

        self.top_result = ''
        self.results_message = 'Your house is... '
        self.table_title = 'For all possible combinations of sorting test questions you could receive, ' \
                           'here are both the number of times and the probability you would get each house:'

        self.title('Hogwarts Sorting Quiz')
        self.geometry('1040x585')
        self.resizable(0, 0)
        self.create_frame()

    def create_frame(self):
        self.frame = tk.Frame()
        self.frame.pack(expand=True)

        # setting up enter label
        if self.q_count == -1:
            self.enter_label = tk.Label(self.frame, wraplength=500, justify='left',
                                        fg='black', pady=10, font=('TkMenuFont', 16))
            self.enter_label.pack()

        # setting up overview label
        if self.q_count == 0:
            self.overview_label = tk.Label(self.frame, wraplength=640, justify='left',
                                           fg='black', pady=10, font=('TkMenuFont', 16))
            self.overview_label.pack()

        # setting up question label
        if 0 < self.q_count <= self.q_total:
            self.question_label = tk.Label(self.frame, wraplength=640, justify='left',
                                           fg='black', pady=10, font=('TkMenuFont', 16))
            self.question_label.pack()

        # setting up the name input
        if self.q_count == -1:
            self.create_textbox()
        # setting up the overview
        elif self.q_count == 0:
            self.create_overview()
        # setting up answer radio choices
        elif self.q_count <= self.q_total:
            self.create_radio()
        # setting up the results page
        elif self.q_count > self.q_total:
            # setting up results labels
            self.results_message_label = tk.Label(self.frame, wraplength=500, justify='left',
                                                  fg='black', pady=20, font=('TkMenuFont', 16))
            self.results_message_label.pack()
            self.results_table_title_label = tk.Label(self.frame, wraplength=500, justify='left',
                                                      fg='black', pady=10, font=('TkMenuFont', 11))
            self.results_table_title_label.pack()

            # setting up tree table
            style = ttk.Style(self.tree)
            style.theme_use('alt')
            style.configure('Treeview', fieldbackground='black')
            style.configure('Treeview.Heading', background='lightgrey', font=('TkMenuFont', 13))

            self.col_names = ['Result', 'Frequency', 'Probability']
            self.tree = ttk.Treeview(self, columns=self.col_names, show='headings', height=5, selectmode='none')
            for i in range(0, len(self.col_names)):
                self.tree.heading(self.col_names[i], text=self.col_names[i])
                self.tree.column(self.col_names[i], width=150, anchor='center')
                if i == 2:
                    self.tree.column(self.col_names[i], anchor='e')
            for i in range(0, len(self.table_data)):
                self.tree.insert('', tk.END, values=self.table_data[i], tags='style')
                self.tree.tag_configure('style', font=('TkTextFont', 11))

            # getting the coordinates for the treeview
            tree_x = (self.winfo_width() - 450) / 2
            self.tree.place(x=tree_x, y=370)

            self.create_results()

        # setting up empty label to put space above the buttons
        if self.q_count <= self.q_total:
            self.empty_label = tk.Label(self.frame, pady=5)
            self.empty_label.pack()

        # setting up the previous button
        if 0 < self.q_count <= self.q_total:
            self.previous_button = tk.Button(self.frame, text='Previous',
                                             state='disabled', command=self.previous)
            if self.q_count > 1:
                self.previous_button['state'] = 'normal'
            self.previous_button.pack(side=tk.LEFT)

        # setting up the next button
        if 0 < self.q_count < self.q_total:
            self.next_button = tk.Button(self.frame, text='Next',
                                         state='disabled', command=self.next)
            if len(self.answers) >= self.q_count:
                self.next_button['state'] = 'normal'
            self.next_button.pack(side=tk.RIGHT)

        # setting up the results button
        if self.q_count == self.q_total:
            self.results_button = tk.Button(self.frame, text='Results!',
                                            state='disabled', command=self.results)
            if len(self.answers) >= self.q_count:
                self.results_button['state'] = 'normal'
            self.results_button.pack(side=tk.RIGHT)

    def create_textbox(self):
        self.enter_label['text'] = 'Enter your name:'
        self.text_box = tk.Text(self.frame, height=2, width=20)
        self.text_box.pack()
        self.enter_button = tk.Button(self.frame, text='Enter',
                                      state='normal', command=self.next)
        self.enter_button.pack(side=tk.BOTTOM)

    def create_overview(self):
        self.overview_label['text'] = 'The Hogwarts Sorting Test, as found on Pottermore.com, sorts you into one of ' \
                                      'the four Hogwarts houses: Gryffindor, Hufflepuff, Ravenclaw, and Slytherin. ' \
                                      'The test does this by asking you eight rounds of questions, with one question ' \
                                      'each round. Each round, however, has multiple possible questions you could ' \
                                      'receive. This means that you would receive a different combination of ' \
                                      'questions each time you took the test, and your result might be different!\n\n' \
                                      'The sorting test you are about to take asks you to answer every possible ' \
                                      'Pottermore sorting question per round rather than just one question per ' \
                                      'round. It then gives you your house results for every possible test ' \
                                      'combination you could receive.\n\nEnjoy!'
        self.start_button = tk.Button(self.frame, text='Start Quiz',
                                      state='normal', command=self.next)
        self.start_button.pack(side=tk.BOTTOM)

    def create_radio(self):
        # making the selected choice a string variable
        self.radio_choice = tk.StringVar()
        # setting the default choice as the user's answer from before, in the case that the 'previous' button is clicked
        if len(self.answers) >= self.q_count:
            self.radio_choice.set(self.answers[self.q_count - 1])
        # otherwise making no choices preselected
        else:
            self.radio_choice.set(None)

        # getting the question and all answer choices from the question block
        question, *choices = self.question_blocks[self.q_count - 1].split('\n')
        # making a label with a number and the question
        self.question_label['text'] = f'{self.q_count}) {question[question.find(""):]}'
        # making a radio option for each answer choice
        for choice in choices:
            tk.Radiobutton(self.frame, text=choice, wraplength=500, font=('TkTextFont', 11),
                           padx=20, variable=self.radio_choice, value=choice, justify='left',
                           command=self.radio).pack(anchor=tk.W)

    def create_results(self):
        # setting up the results labels
        results_message = self.results_message + self.top_result + '!'
        self.results_message_label['text'] = results_message
        self.results_table_title_label['text'] = self.table_title

    # what happens when a radio choice is selected
    def radio(self):
        # allowing the next button to be clicked
        if self.q_count < self.q_total:
            self.next_button['state'] = 'normal'
        else:
            self.results_button['state'] = 'normal'
        # replacing any preexisting answer choice in list of answers with the new selection
        if len(self.answers) >= self.q_count != 0:
            self.answers[self.q_count - 1] = self.radio_choice.get()
        # or adding the selected answer choice to list of answers the first time a question is answered
        else:
            self.answers.append(self.radio_choice.get())

    # what happens when the next button is clicked
    def next(self):
        # handling file name from user's input of name
        if self.q_count == -1:
            self.name = self.text_box.get(1.0, 'end-1c')
            self.file_name = self.name.strip().lower() + '_answers.txt'

        # always happens
        self.frame.destroy()
        self.q_count += 1
        self.create_frame()

    # what happens when the previous button is clicked
    def previous(self):
        self.frame.destroy()
        self.q_count -= 1
        self.create_frame()

    # what happens when the results button is clicked
    def results(self):
        self.frame.destroy()
        # writing answers into answer file
        answer_file = open(self.file_name, 'w', encoding='utf-8')
        answer_file.seek(0)
        answer_file.truncate(0)
        for answer in self.answers:
            answer_file.write(answer)
            answer_file.write('\n')
        answer_file.close()
        self.q_count += 1

        # using sorting_analysis.py
        # pulling in the answer weights and the user's answers, returning a dataframe of dictionaries
        weights_file = "Pottermore Sorting Quiz weights.csv"
        df_dict = answers_and_weights(weights_file, self.file_name)

        # separating the questions with chosen answers by round
        answer_choices_list = separate_by_round(df_dict)

        # calculating all the combinations of total scores
        combination_scores_list = get_all_score_combinations(answer_choices_list)

        # calculating the frequency and probability of each outcome
        self.table_data = calculate_results(combination_scores_list)

        # calculating the top result
        self.top_result = max_value(self.table_data)

        self.create_frame()
