import json
import logging
import re
from collections import defaultdict
from pathlib import Path

import keyboard


# Add contests and stop program
class ButtonActions:
    # Stop program
    def __on_press_stop(self):
        logging.debug('Script is stopped')
        self.exit_program = True

    # Add contest
    @staticmethod
    def __on_press_add_contests():
        # Type of contests
        print('Enter type of contests:')
        type_of_contest = input()

        print('Enter system of contests:')
        contest_system = input()

        # Read list of contests and turn it into dict (type of contests -> contests system -> list of contests)
        print('Enter contests id:')
        add_contests_id = list(map(int, input().split(' ')))
        add = defaultdict(lambda: defaultdict(list))

        for add_contest in add_contests_id:
            add[type_of_contest][contest_system].append(add_contest)

        # Read JSON-file with contests id (type of contests -> list of contests)
        if Path('cache/id.json').stat().st_size != 0:
            read_id = open('cache/id.json')
            dict_id = json.load(read_id)
            read_id.close()

            for contest in dict_id.keys():
                for contest_system in dict_id[contest].keys():
                    for contest_id in dict_id[contest][contest_system]:
                        add[contest][contest_system].append(contest_id)

        # Update JSON-file with contests id (type of contests -> list of contests)
        write_id = open('cache/id.json', 'w')
        json.dump(add, write_id)
        write_id.close()

        logging.debug(f'added contests with id = {add_contests_id} of type {type_of_contest}')

    # Adding coefficients.json to the total mark
    @staticmethod
    def __on_press_add_coefficients():
        print('Enter type of contest and coefficient')
        contest_type, coefficient = re.split('[ ,;:]', input())

        if Path('cache/coefficients.json').stat().st_size != 0:
            read_coefficients = open('cache/coefficients.json')
            dict_coefficients = json.load(read_coefficients)
            read_coefficients.close()
        else:
            dict_coefficients = dict()

        dict_coefficients[contest_type] = float(coefficient)

        write_coefficients = open('cache/coefficients.json', 'w')
        json.dump(dict_coefficients, write_coefficients)
        write_coefficients.close()

        logging.debug(f'added contest type {contest_type} with coefficient {coefficient}')

    # Add hotkeys
    def __init__(self):
        self.exit_program = False
        keyboard.add_hotkey('ctrl+alt+x', self.__on_press_stop)
        keyboard.add_hotkey('ctrl+alt+d', self.__on_press_add_contests)
        keyboard.add_hotkey('ctrl+a+c', self.__on_press_add_coefficients)
