# This file brings in the weights of the sorting questions and calculates frequencies and probabilities based on answers

# csv originally downloaded from the following site, then edited:
# "https://www.reddit.com/r/Pottermore/comments/8rgo4d/new_finding_on_the_grading_scheme_of_the_sorting/"

import csv


# weights file is "Pottermore Sorting Quiz weights.csv"
# opens weights file and answers file. adds user's answers in weights file
def answers_and_weights(weights_file, answers_file):
    # open the csv into a file and convert each row to dicts with keys of column headers and values of rows
    with open(weights_file, 'r', encoding='windows-1252') as file:
        csv_to_dicts = csv.DictReader(file)
        df_dict = list(csv_to_dicts)

    user_answers_file = answers_file
    user_answers_list = open(user_answers_file, encoding='windows-1252').read().rstrip().split('\n')

    for dictio in df_dict:
        if dictio['Answer'] in user_answers_list:
            dictio['choice'] = "yes"
        else:
            dictio['choice'] = "no"

    return df_dict


def separate_by_round(answers_weights_dict):
    round1 = []
    round2 = []
    round3 = []
    round4 = []
    round5 = []
    round6 = []
    round7 = []
    round8 = []

    # making lists of dictionaries separated by round for the selected answers
    answer_choices_list = [round1, round2, round3, round4, round5, round6, round7, round8]

    for dictio in answers_weights_dict:
        for i in range(8):
            if int(dictio['Round No']) == i + 1 and dictio['choice'] == "yes":
                answer_choices_list[i].append(dictio)

    return answer_choices_list


def get_all_score_combinations(answers_by_rounds_list):

    # calculating all the combinations
    combinations_scores_list = []
    # making the score counters
    g_score = 0
    h_score = 0
    r_score = 0
    s_score = 0

    # adding up the scores
    for question1 in answers_by_rounds_list[0]:
        for question2 in answers_by_rounds_list[1]:
            for question3 in answers_by_rounds_list[2]:
                for question4 in answers_by_rounds_list[3]:
                    for question5 in answers_by_rounds_list[4]:
                        for question6 in answers_by_rounds_list[5]:
                            for question7 in answers_by_rounds_list[6]:
                                for question8 in answers_by_rounds_list[7]:
                                    g_score += float(question1['Gryffindor Weight']) + float(question2['Gryffindor Weight']) + float(question3['Gryffindor Weight']) + float(question4['Gryffindor Weight']) + float(question5['Gryffindor Weight']) + float(question6['Gryffindor Weight']) + float(question7['Gryffindor Weight']) + float(question8['Gryffindor Weight'])
                                    h_score += float(question1['Hufflepuff Weight']) + float(question2['Hufflepuff Weight']) + float(question3['Hufflepuff Weight']) + float(question4['Hufflepuff Weight']) + float(question5['Hufflepuff Weight']) + float(question6['Hufflepuff Weight']) + float(question7['Hufflepuff Weight']) + float(question8['Hufflepuff Weight'])
                                    r_score += float(question1['Ravenclaw Weight']) + float(question2['Ravenclaw Weight']) + float(question3['Ravenclaw Weight']) + float(question4['Ravenclaw Weight']) + float(question5['Ravenclaw Weight']) + float(question6['Ravenclaw Weight']) + float(question7['Ravenclaw Weight']) + float(question8['Ravenclaw Weight'])
                                    s_score += float(question1['Slytherin Weight']) + float(question2['Slytherin Weight']) + float(question3['Slytherin Weight']) + float(question4['Slytherin Weight']) + float(question5['Slytherin Weight']) + float(question6['Slytherin Weight']) + float(question7['Slytherin Weight']) + float(question8['Slytherin Weight'])
                                    # making a list of the score counters
                                    combination_list = [g_score, h_score, r_score, s_score]
                                    combinations_scores_list.append(combination_list)
                                    # resetting the score counters
                                    g_score = 0
                                    h_score = 0
                                    r_score = 0
                                    s_score = 0

    return combinations_scores_list


def calculate_results(all_score_combinations_list):

    g_counter = 0
    h_counter = 0
    r_counter = 0
    s_counter = 0
    tie_counter = 0
    # gh_counter = 0
    # gr_counter = 0
    # gs_counter = 0
    # hr_counter = 0
    # hs_counter = 0
    # rs_counter = 0
    # ghr_counter = 0
    # ghs_counter = 0
    # grs_counter = 0
    # hrs_counter = 0
    # ghrs_counter = 0

    for i in all_score_combinations_list:
        # Gryffindor win
        if i[0] > i[1] and i[0] > i[2] and i[0] > i[3]:
            g_counter += 1
        # Hufflepuff win
        elif i[0] < i[1] and i[1] > i[2] and i[1] > i[3]:
            h_counter += 1
        # Ravenclaw win
        elif i[0] < i[2] and i[1] < i[2] and i[2] > i[3]:
            r_counter += 1
        # Slytherin win
        elif i[0] < i[3] and i[1] < i[3] and i[2] < i[3]:
            s_counter += 1
        else:
            tie_counter += 1
        # Gryffindor and Hufflepuff tie
        # elif i[0] == i[1] > i[2] and i[0] > i[3]:
        #     gh_counter += 1
        # # Gryffindor and Ravenclaw tie
        # elif i[0] == i[2] > i[1] and i[0] > i[3]:
        #     gr_counter += 1
        # # Gryffindor and Slytherin tie
        # elif i[0] == i[3] > i[1] and i[0] > i[2]:
        #     gs_counter += 1
        # # Hufflepuff and Ravenclaw tie
        # elif i[0] < i[1] == i[2] and i[1] > i[3]:
        #     hr_counter += 1
        # # Hufflepuff and Slytherin tie
        # elif i[0] < i[1] == i[3] and i[1] > i[2]:
        #     hs_counter += 1
        # # Ravenclaw and Slytherin tie
        # elif i[0] < i[2] == i[3] and i[1] < i[2]:
        #     rs_counter += 1
        # # All tie except Slytherin
        # elif i[0] == i[1] == i[2] > i[3]:
        #     ghr_counter += 1
        # # All tie except Ravenclaw
        # elif i[0] == i[1] == i[3] > i[2]:
        #     ghs_counter += 1
        # # All tie except Hufflepuff
        # elif i[0] == i[2] == i[3] > i[1]:
        #     grs_counter += 1
        # # All tie except Gryffindor
        # elif i[0] < i[1] == i[2] == i[3]:
        #     hrs_counter += 1
        # # All tie
        # else:
        #     ghrs_counter += 1

    # table with results
    col_names = ["Result", "Frequency", "Probability"]

    table_data = [["Gryffindor", g_counter, round(g_counter / 9720, 12)],
                  ["Hufflepuff", h_counter, round(h_counter / 9720, 12)],
                  ["Ravenclaw", r_counter, round(r_counter / 9720, 12)],
                  ["Slytherin", s_counter, round(s_counter / 9720, 12)],
                  ["Ties", tie_counter, round(tie_counter / 9720, 12)]]
                  # ["Gryffindor/Hufflepuff Tie", gh_counter, gh_counter / 9720],
                  # ["Gryffindor/Ravenclaw Tie", gr_counter, gr_counter / 9720],
                  # ["Gryffindor/Slytherin Tie", gs_counter, gs_counter / 9720],
                  # ["Hufflepuff/Ravenclaw Tie", hr_counter, hr_counter / 9720],
                  # ["Hufflepuff/Slytherin Tie", hs_counter, hs_counter / 9720],
                  # ["Ravenclaw/Slytherin Tie", rs_counter, rs_counter / 9720],
                  # ["Gryffindor/Hufflepuff/Ravenclaw Tie", ghr_counter, ghr_counter / 9720],
                  # ["Gryffindor/Ravenclaw/Slytherin Tie", grs_counter, grs_counter / 9720],
                  # ["Hufflepuff/Ravenclaw/Slytherin Tie", hrs_counter, hrs_counter / 9720],
                  # ["Gryffindor/Hufflepuff/Ravenclaw/Slytherin Tie", ghrs_counter, ghrs_counter / 9720]]

    return table_data


def max_value(outcomes_list):
    max_outcome = max([outcome[1] for outcome in outcomes_list])
    count = 0
    winner = []
    winner_string = ''
    for outcome in outcomes_list:
        if outcome[1] == max_outcome:
            count += 1
            winner.append(outcome[0])
    if len(winner) == 1:
        winner_string = winner[0]
    elif len(winner) == 2:
        winner_string = winner[0] + ' and ' + winner[1]
    else:
        commas = len(winner) - 1
        while commas > 0:
            winner_string += winner[len(winner) - commas - 1] + ', '
            commas -= 1
        winner_string += 'and ' + winner[-1]
    return winner_string
