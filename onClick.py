import json
import logging
from collections import defaultdict

import keyboard


# Add contests and stop program
class ButtonActions:
    # Stop program
    def on_press_stop(self):
        logging.debug('Script is stopped')
        self.exit_program = True

    # Add contest
    @staticmethod
    def __on_press_add_contests(type_of_contest: str):
        # Read list of contests and turn it into dict (type of contests -> list of contests)
        add_contests_id = list(map(int, input().split(' ')))
        add = defaultdict(list)

        for add_contest in add_contests_id:
            add[type_of_contest].append(add_contest)

        # Read JSON-file with contests id (type of contests -> list of contests)
        read_id = open('cache/id.json')
        dict_id = json.load(read_id)
        read_id.close()

        for contest_type in dict_id.keys():
            for contest in dict_id[contest_type]:
                add[contest_type].append(contest)

        # Update JSON-file with contests id (type of contests -> list of contests)
        write_id = open('cache/id.json', 'w')
        json.dump(add, write_id)
        write_id.close()

        logging.debug(f'added contests with id = {add_contests_id} of type {type_of_contest}')

    # Thematic contests hotkey
    def thematic_contests(self):
        self.__on_press_add_contests('thematic')

    # Command contests upsolving hotkey
    def command_contests(self):
        self.__on_press_add_contests('command')

    # Scoring contests hotkey
    def scoring_contests(self):
        self.__on_press_add_contests('scoring')

    # Add hotkeys
    def __init__(self):
        self.exit_program = False
        keyboard.add_hotkey('ctrl+alt+x', self.on_press_stop)
        keyboard.add_hotkey('ctrl+a+t', self.thematic_contests)
        keyboard.add_hotkey('ctrl+a+i', self.scoring_contests)
        keyboard.add_hotkey('ctrl+a+c', self.command_contests)
