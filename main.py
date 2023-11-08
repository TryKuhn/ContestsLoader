import logging
import sys
import time
from collections import defaultdict

import pandas as pd

from GetCoefficients import get_coefficients
from UpdateFinal import update_final
from apiCodeforces import CodeforcesApi
from getContestsId import get_contests_id
from onClick import ButtonActions
from updateContests import update_contests

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

api = CodeforcesApi()
api.load_info('https://codeforces.com')

button = ButtonActions()

while not button.exit_program:

    total_result = defaultdict(list)
    order_of_key = dict()

    contests_id = get_contests_id()
    update_contests(contests_id)
    logging.debug(f'contests standings are updated')

    coefficients = get_coefficients()
    update_final(coefficients)

    total_result = pd.DataFrame(total_result)

    writer = pd.ExcelWriter('standings.xlsx')
    total_result.to_excel(writer, f'total')
    writer.close()

    time.sleep(10)
