from sorting_interface import Sorting


# pulling in the questions and answers file and running the test
sorting_questions_file = 'questions_answers.txt'
question_answers_groups = open(sorting_questions_file, encoding='utf-8').read().rstrip().split('\n\n')

interface_sorting = Sorting(question_answers_groups)
interface_sorting.mainloop()
