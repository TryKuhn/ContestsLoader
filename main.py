import logging
import sys
import time

import pandas as pd

import data
from GetCoefficients import get_coefficients
from UpdateFinal import update_final
from getContestsId import get_contests_id
from onClick import ButtonActions
from updateContests import update_contests

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

button = ButtonActions()

# Main program
while not button.exit_program:
    # Initialize data
    data.init()

    # Get contests by API
    data.contests_id = get_contests_id()
    update_contests()

    # Update table and write sheets with contests
    data.coefficients = get_coefficients()
    update_final()

    # Sort sheet 'total' by descending and convert to excel
    data.total_result = pd.DataFrame(data.total_result)
    data.total_result.sort_values(by='total', ascending=False, inplace=True)
    data.total_result.to_excel(data.writer, 'total')

    # Close writer
    data.writer.close()

    # Wait till next update
    logging.debug(f'contests standings are updated')
    time.sleep(10)
