import main
from getTotalByType import getTotalTable
from main import api, writer, order_of_key
import pandas as pd
from makeTable import normalise_file


# Update all contests standings
def update_contests(contests_id):
    for contests_type in contests_id.keys():
        for contest_id in contests_id[contests_type]:
            standings = api.get_standings(contest_id)

            score = len(standings['problems'])
            if standings['contest']['type'] == 'IOI':
                score = 0
                if len(standings['rows']) != 0:
                    for problem in standings['rows'][0]['problemResults']:
                        score += int(problem['points'])
                if score == 0:
                    score = 1

            standings_dict = normalise_file(standings['rows'], score)

            main.total_result = getTotalTable(standings_dict, order_of_key, contests_type, main.total_result)

            final_result_df = pd.DataFrame(standings_dict)
            final_result_df.to_excel(writer, f'contest{contest_id}')
