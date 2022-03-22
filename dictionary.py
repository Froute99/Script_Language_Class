

import random


def generate_scores():
    scores = [
                 {'kor': random.randint(0, 100),
                  'eng': random.randint(0, 100),
                  'math': random.randint(0, 100)} for i in range(20)]
    pass


def process_scores():
    pass


def print_scores():
    pass


generate_scores()
process_scores()
print_scores()
