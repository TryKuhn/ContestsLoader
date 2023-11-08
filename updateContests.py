import data
from getTotalByType import getTotalTable
import pandas as pd
from makeTable import normalise_file


# Update all contests standings
def update_contests():
    for contests_type in data.contests_id.keys():
        for contest_id in data.contests_id[contests_type]:
            standings = data.api.get_standings(contest_id)

            score = len(standings['problems'])
            if standings['contest']['type'] == 'IOI':
                score = 0
                if len(standings['rows']) != 0:
                    for problem in standings['rows'][0]['problemResults']:
                        score += int(problem['points'])
                if score == 0:
                    score = 1

            standings_dict = normalise_file(standings['rows'], score)

            data.total_result = getTotalTable(standings_dict, data.order_of_key, contests_type, data.total_result)

            final_result_df = pd.DataFrame(standings_dict)
            final_result_df.to_excel(data.writer, f'contest{contest_id}')
