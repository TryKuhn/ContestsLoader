from main import api
import pandas as pd
from makeTable import normalise_file


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


            final_result_df = pd.DataFrame(standings_dict)
            final_result_df.to_excel(writer, f'contest{contest_id}')
