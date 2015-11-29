import os
import sys
import random

'''
class Choice():

    randomize = True
    correct = False
    text = ''

    def __init__(self, randomize, correct, text):
        self.randomize = randomize
        self.correct = correct
        self.text = text


class Question():

    choices = []
    randomize = True
    text = ''

    def __init__(self, randomize=True):
        self.randomize = randomize

'''

if os.path.exists(sys.argv[1]):
    with open(sys.argv[1], 'rb') as f:
        exam_text = f.read().decode('utf-8')
else:
    sys.exit('File not found :' + sys.argv[1])

questions_text = exam_text.split('\\begin{questions}')[1]\
    .split('\\end{questions}')[0].split('\\question')

questions_text = [x.strip() for x in questions_text if not x.isspace()]

random.shuffle(questions_text)

for question_text in questions_text:
    q_text = question_text.split('\\begin{choices}')[0].strip()
    choices_text = question_text.split('\\begin{choices}')[1]\
        .split('\\end{choices}')[0]
    choices = choices_text.split('\n')
    choices = [x.strip() for x in choices if not x.isspace()]
    random.shuffle(choices)
    print('''\\question {0}
\\begin{{choices}}
{1}
\\end{{choices}}'''.format(q_text, "\n".join(choices)))
    print('\n')
