import functions
import string


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    group_answers = functions.get_data_from_string(input, '\n\n')
    yes_answers = []
    sum = 0

    for group_answer in group_answers:
        answers = functions.get_data_from_string(group_answer)
        member = len(answers)
        yes = 0
        questions = {}

        for i, answer in enumerate(answers):
            letters = functions.split_string(answer)

            if i == 0:
                for letter in letters:
                    if letter not in questions:
                        questions[letter] = 1

                continue

            for letter in letters:
                if letter not in questions:
                    questions[letter] = 1
                else:
                    questions[letter] += 1

        for char in questions:
            num = questions[char]
            if num == member:
                yes += 1

        yes_answers.append(yes)

    for yes_answer in yes_answers:
        sum += yes_answer

    return sum
